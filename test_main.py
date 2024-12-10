import pytest
from fastapi.testclient import TestClient
from app.app import app  # Import your FastAPI app

client = TestClient(app)

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "Real Estate Price Estimator" in response.text

def test_predict_price():
    # Sample input for prediction
    input_data = {
        "lot_area": 1500,
        "quality": 7,
        "condition": 8,
        "central_air": 1,
        "full_bath": 2,
        "bedrooms": 3,
        "garage_cars": 2
    }
    
    response = client.post("/predict", json=input_data)  # Update route if needed
    assert response.status_code == 200
    assert "Estimated Sale Price" in response.json()

def test_invalid_input():
    # Invalid input (missing required field)
    input_data = {
        "lot_area": 1500,
        "quality": 7,
        "condition": 8,
        "central_air": True,
        # Missing full_bath, bedrooms, garage_cars
    }

    response = client.post("/predict", json=input_data)
    assert response.status_code == 422  # Unprocessable Entity for invalid input

@pytest.mark.parametrize("lot_area,quality,condition,expected_status", [
    (1500, 7, 8, 200),
    (2000, 9, 10, 200),
    (500, 5, 5, 200),
    ("s", 10, 10, 422),  # Invalid input, might return a 422 error if validation fails
])
def test_predict_parametrized(lot_area, quality, condition, expected_status):
    input_data = {
        "lot_area": lot_area,
        "quality": quality,
        "condition": condition,
        "central_air": 1,
        "full_bath": 2,
        "bedrooms": 3,
        "garage_cars": 2
    }
    
    response = client.post("/predict", json=input_data)
    assert response.status_code == expected_status
    if expected_status == 200:
        assert "Estimated Sale Price" in response.json()
