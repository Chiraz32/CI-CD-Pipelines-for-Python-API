import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_celsius_to_fahrenheit():
    response = client.get("/celsius-to-fahrenheit?value=0")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(32)

    response = client.get("/celsius-to-fahrenheit?value=100")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(212)

def test_fahrenheit_to_celsius():
    response = client.get("/fahrenheit-to-celsius?value=32")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(0)

    response = client.get("/fahrenheit-to-celsius?value=212")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(100)

def test_celsius_to_kelvin():
    response = client.get("/celsius-to-kelvin?value=0")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(273.15)

    response = client.get("/celsius-to-kelvin?value=100")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(373.15)

def test_kelvin_to_celsius():
    response = client.get("/kelvin-to-celsius?value=273.15")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(0)

    response = client.get("/kelvin-to-celsius?value=373.15")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(100)

def test_fahrenheit_to_kelvin():
    response = client.get("/fahrenheit-to-kelvin?value=32")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(273.15)

    response = client.get("/fahrenheit-to-kelvin?value=212")
    assert response.status_code == 200
    assert response.json()["output"] == pytest.approx(373.15)


