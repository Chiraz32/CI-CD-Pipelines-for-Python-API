import pytest
from main import TemperatureConverter

def test_celsius_to_fahrenheit():
    assert TemperatureConverter.celsius_to_fahrenheit(0) == pytest.approx(32)
    assert TemperatureConverter.celsius_to_fahrenheit(100) == pytest.approx(212)

def test_fahrenheit_to_celsius():
    assert TemperatureConverter.fahrenheit_to_celsius(32) == pytest.approx(0)
    assert TemperatureConverter.fahrenheit_to_celsius(212) == pytest.approx(100)

def test_celsius_to_kelvin():
    assert TemperatureConverter.celsius_to_kelvin(0) == pytest.approx(273.15)
    assert TemperatureConverter.celsius_to_kelvin(100) == pytest.approx(373.15)

