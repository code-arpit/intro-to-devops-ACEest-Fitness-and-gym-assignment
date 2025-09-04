import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Add a Workout" in response.data


def test_add_workout_valid(client):
    response = client.post(
        "/", data={"workout": "Running", "duration": "30"}, follow_redirects=True
    )
    assert response.status_code == 200
    # assert b"'Running' added successfully!" in response.data
    # assert b"Running - 30 minutes" in response.data


def test_add_workout_missing_fields(client):
    response = client.post(
        "/", data={"workout": "", "duration": ""}, follow_redirects=True
    )
    assert b"Please enter both workout and duration." in response.data


def test_add_workout_invalid_duration(client):
    response = client.post(
        "/", data={"workout": "Cycling", "duration": "abc"}, follow_redirects=True
    )
    assert b"Duration must be a number." in response.data
