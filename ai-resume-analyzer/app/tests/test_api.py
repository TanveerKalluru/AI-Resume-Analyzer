from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_resume_parsing():
    response = client.post("/api/v1/resume/parse", json={"resume": "sample_resume_text"})
    assert response.status_code == 200
    assert "parsed_data" in response.json()

def test_ats_scoring():
    response = client.post("/api/v1/resume/ats_score", json={"resume": "sample_resume_text"})
    assert response.status_code == 200
    assert "score" in response.json()

def test_ai_feedback_generation():
    response = client.post("/api/v1/resume/feedback", json={"resume": "sample_resume_text"})
    assert response.status_code == 200
    assert "feedback" in response.json()

def test_resume_qna():
    response = client.post("/api/v1/resume/qna", json={"question": "What is the candidate's experience?"})
    assert response.status_code == 200
    assert "answer" in response.json()