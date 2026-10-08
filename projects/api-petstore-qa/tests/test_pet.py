import requests
import pytest

from data.pet_data import PET_VALID, PET_MULTIPLE_PHOTOS, PET_INVALID_STATUS, PET_MISSING_NAME, PET_EMPTY, PET_EMPTY_PHOTOS, PET_INVALID_ID_TYPE, PET_EMPTY_STATUS


def test_create_pet():
    def test_create_pet():
        url = "https://petstore.swagger.io/v2/pet"
        response = requests.post(url, json=PET_VALID)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["id"] == 158
        assert response_data["name"] == "max"
        assert response_data["category"]["name"] == "dogs"
        assert response_data["photoUrls"][0] == "https://example.com/max.jpg"
        assert response_data["tags"][0]["name"] == "friendly"
        assert response_data["status"] == "available"

def test_create_pet_multiple_photos():
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=PET_MULTIPLE_PHOTOS)
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["photoUrls"]) == 2
    assert response_data["photoUrls"][0] == "https://example.com/max1.jpg"
    assert response_data["photoUrls"][1] == "https://example.com/max2.jpg"

@pytest.mark.xfail(reason="BUG-001: API acepta un status no válido")
def test_create_pet_invalid_status():
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=PET_INVALID_STATUS)
    assert response.json()["status"] != "sold123"

@pytest.mark.xfail(reason="BUG-002: API acepta una mascota sin el campo name")
def test_create_pet_missing_name():
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=PET_MISSING_NAME)
    assert "name" in response.json()

@pytest.mark.xfail(reason="BUG-003: API acepta un body vacío")
def test_create_pet_empty_body():
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=PET_EMPTY)
    assert response.json()["id"] is None

def test_create_pet_empty_photos():
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=PET_EMPTY_PHOTOS)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == 162
    assert response_data["name"] == "max5"
    assert response_data["photoUrls"] == []
    assert response_data["status"] == "available"

@pytest.mark.xfail(reason="BUG-004: API devuelve 500 ante un id con tipo de dato inválido")
def test_create_pet_invalid_id_type():
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=PET_INVALID_ID_TYPE)
    assert response.status_code != 500

@pytest.mark.xfail(reason="BUG-005: API acepta un status vacío")
def test_create_pet_empty_status():
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json=PET_EMPTY_STATUS)
    assert response.json()["status"] != ""



