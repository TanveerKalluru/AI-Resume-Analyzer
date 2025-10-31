from sqlalchemy.orm import Session
from app.models.resume import Resume
from app.schemas.resume import ResumeCreate, ResumeUpdate

class ResumeRepository:
    """Repository for interacting with the Resume data in the database."""

    def __init__(self, db: Session):
        """Initialize the repository with a database session.

        Args:
            db (Session): The database session to use for operations.
        """
        self.db = db

    def create_resume(self, resume: ResumeCreate) -> Resume:
        """Create a new resume in the database.

        Args:
            resume (ResumeCreate): The resume data to create.

        Returns:
            Resume: The created resume object.
        """
        db_resume = Resume(**resume.dict())
        self.db.add(db_resume)
        self.db.commit()
        self.db.refresh(db_resume)
        return db_resume

    def get_resume(self, resume_id: int) -> Resume:
        """Retrieve a resume by its ID.

        Args:
            resume_id (int): The ID of the resume to retrieve.

        Returns:
            Resume: The retrieved resume object, or None if not found.
        """
        return self.db.query(Resume).filter(Resume.id == resume_id).first()

    def update_resume(self, resume_id: int, resume_update: ResumeUpdate) -> Resume:
        """Update an existing resume in the database.

        Args:
            resume_id (int): The ID of the resume to update.
            resume_update (ResumeUpdate): The updated resume data.

        Returns:
            Resume: The updated resume object, or None if not found.
        """
        db_resume = self.get_resume(resume_id)
        if db_resume:
            for key, value in resume_update.dict(exclude_unset=True).items():
                setattr(db_resume, key, value)
            self.db.commit()
            self.db.refresh(db_resume)
        return db_resume

    def delete_resume(self, resume_id: int) -> bool:
        """Delete a resume from the database.

        Args:
            resume_id (int): The ID of the resume to delete.

        Returns:
            bool: True if the resume was deleted, False otherwise.
        """
        db_resume = self.get_resume(resume_id)
        if db_resume:
            self.db.delete(db_resume)
            self.db.commit()
            return True
        return False

    def get_all_resumes(self) -> list[Resume]:
        """Retrieve all resumes from the database.

        Returns:
            list[Resume]: A list of all resume objects.
        """
        return self.db.query(Resume).all()