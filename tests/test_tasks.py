from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

def test_create_task():
    payload = {
        "title": "Learn SonarQube",
        "description": "Testing DevSecOps pipeline"
    }

    response = client.post("/tasks", json=payload)

    assert response.status_code == 200