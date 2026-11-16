"""Tests the health API endpoint with pytest"""
from PRO2002WorkRequirement4.app import app

def test_api_status_and_json_response():
    """Validates that the health API endpoint returns HTTP 200 status code and the response body"""

    # Creating a Flask test client for the test
    client = app.test_client()

    # Sends a GET request to the health API endpoint
    response = client.get("/health")

    # Controls that the health API endpoint returns HTTP 200 and the JSON response
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
