import requests
import pytest
import json
import jsonschema
from jsonschema import validate


BASE_URL = "http://localhost:8080"

@pytest.mark.api
def test_unauthorized_scenario():
    response = requests.get(f"{BASE_URL}/product?scenario=unauthorized")
    assert response.status_code == 401
    assert "Unauthorized" in response.json()["message"]
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"}
        },
        "required": ["message"]
    }
    validate(instance=response.json(), schema=schema, format_checker=jsonschema.FormatChecker())

@pytest.mark.api
def test_service_unavailable_scenario():
    response = requests.get(f"{BASE_URL}/product?scenario=serviceUnavailable")
    assert response.status_code == 503
    assert "Service Unavailable" in response.json()["message"]
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"}
        },
        "required": ["message"]
    }
    validate(instance=response.json(), schema=schema, format_checker=jsonschema.FormatChecker())


@pytest.mark.api
def test_successful_scenario():
    response = requests.get(f"{BASE_URL}/product")
    assert response.status_code == 200
    assert len(response.json()) > 0
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                },
                "description": {
                    "type": "string",
                    "enum": [
                        "Lorem ipsum dolor sit amet."
                    ]
                },
                "price": {
                    "type": "integer"
                },
                "isBasketDiscount": {
                    "type": "boolean"
                },
                "basketDiscountPercentage": {
                    "type": "integer"
                },
                "rating": {
                    "type": "number"
                },
                "stock": {
                    "type": "integer"
                },
                "isActive": {
                    "type": "boolean"
                },
                "brand": {
                    "type": "string",
                    "enum": [
                        "Apple"
                    ]
                },
                "category": {
                    "type": "string"
                },
                "images": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "id",
                "title",
                "description",
                "price",
                "isBasketDiscount",
                "rating",
                "stock",
                "brand",
                "category",
                "images"
            ]
        }
    }
    validate(instance=response.json(), schema=schema)

# if __name__ == "__main__":
#     test_successful_scenario()
#     test_unauthorized_scenario()
#     test_service_unavailable_scenario()
#     print("All tests passed!")
