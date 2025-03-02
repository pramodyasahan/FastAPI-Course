from fastapi.testclient import TestClient
from TodoApp.app import app
from fastapi import status

client = TestClient(app)


def test_health():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "healthy"}
