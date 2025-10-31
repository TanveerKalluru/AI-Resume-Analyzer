from pydantic import BaseModel
from typing import Optional, List

class ResumeBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    summary: Optional[str] = None
    skills: List[str] = []
    experience: List[str] = []
    education: List[str] = []

class ResumeCreate(ResumeBase):
    pass

class Resume(ResumeBase):
    id: int

    class Config:
        orm_mode = True