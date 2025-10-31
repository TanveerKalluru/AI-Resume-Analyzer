# Contents of /ai-resume-analyzer/ai-resume-analyzer/app/tests/test_services.py

import pytest
from app.services.analyzer import analyze_resume
from app.schemas.resume import ResumeSchema

@pytest.fixture
def sample_resume():
    return ResumeSchema(
        name="John Doe",
        email="john.doe@example.com",
        phone="123-456-7890",
        education="Bachelor of Science in Computer Science",
        experience="5 years of experience in software development",
        skills=["Python", "FastAPI", "Machine Learning"]
    )

def test_analyze_resume(sample_resume):
    """Test the analyze_resume function with a sample resume."""
    result = analyze_resume(sample_resume)
    assert result is not None
    assert isinstance(result, dict)
    assert "score" in result
    assert "feedback" in result

def test_analyze_resume_empty(sample_resume):
    """Test analyze_resume with an empty resume."""
    empty_resume = ResumeSchema(
        name="",
        email="",
        phone="",
        education="",
        experience="",
        skills=[]
    )
    result = analyze_resume(empty_resume)
    assert result is not None
    assert result["score"] == 0
    assert result["feedback"] == "Resume is empty."