from fastapi.testclient import TestClient

from app import app

fake_app = TestClient(app)


def test_index():
    resp = fake_app.get('/')
    assert resp.json() == "Hello, world"
