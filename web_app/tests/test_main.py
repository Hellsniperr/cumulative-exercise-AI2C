"""Tests for the FastAPI web app."""

from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from web_app.main import app

client = TestClient(app)


def test_root_returns_hello_world():
    """The root endpoint returns the expected greeting."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_geocode_returns_coordinates(mocker):
    """The geocode endpoint returns lat/long from the external API."""
    fake_response = MagicMock()
    fake_response.json.return_value = [{"lat": "40.4406", "lon": "-79.9959"}]

    mocker.patch("web_app.main.requests.get", return_value=fake_response)

    response = client.post("/geocode/Pittsburgh/PA")

    assert response.status_code == 200
    assert response.json() == {"lat": "40.4406", "long": "-79.9959"}
