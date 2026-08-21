"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient
from web_app.main import app

client = TestClient(app)

def test_root_returns_hello_world():
    """The root endpoint should return the expected greeting."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}
