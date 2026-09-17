from fastapi.testclient import TestClient

from apps.api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "virogenai-api",
        "version": "0.1.0",
    }


def test_ready() -> None:
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"
