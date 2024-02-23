from fastapi.testclient import TestClient
from app.core.config import settings


def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello World from {settings.APP_NAME}"}