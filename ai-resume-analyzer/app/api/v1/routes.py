from fastapi import APIRouter, HTTPException
from app.schemas.resume import ResumeCreate, ResumeResponse
from app.services.analyzer import analyze_resume
from app.services.embeddings import generate_embeddings

router = APIRouter()

@router.post("/parse", response_model=ResumeResponse)
async def parse_resume(resume: ResumeCreate):
    """
    Parse the provided resume and return structured data.

    Args:
        resume (ResumeCreate): The resume data to be parsed.

    Returns:
        ResumeResponse: The structured resume data.
    """
    try:
        parsed_data = await analyze_resume(resume)
        return parsed_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/score", response_model=dict)
async def score_resume(resume: ResumeCreate):
    """
    Score the provided resume based on ATS criteria.

    Args:
        resume (ResumeCreate): The resume data to be scored.

    Returns:
        dict: The ATS score and feedback.
    """
    try:
        score = await analyze_resume(resume, scoring=True)
        return {"score": score}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/feedback", response_model=dict)
async def generate_feedback(resume: ResumeCreate):
    """
    Generate AI feedback for the provided resume.

    Args:
        resume (ResumeCreate): The resume data for feedback generation.

    Returns:
        dict: The AI-generated feedback.
    """
    try:
        feedback = await generate_embeddings(resume)
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/qa", response_model=dict)
async def qa_on_resume(question: str, resume: ResumeCreate):
    """
    Answer a question based on the provided resume.

    Args:
        question (str): The question to be answered.
        resume (ResumeCreate): The resume data to reference.

    Returns:
        dict: The answer to the question.
    """
    try:
        answer = await analyze_resume(resume, question=question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))