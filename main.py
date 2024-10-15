from fastapi import FastAPI

app = FastAPI()

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9


    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        return celsius + 273.15


    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

# Mapping paths to converter functions
conversion_functions = {
    "celsius-to-fahrenheit": TemperatureConverter.celsius_to_fahrenheit,
    "fahrenheit-to-celsius": TemperatureConverter.fahrenheit_to_celsius,
    "celsius-to-kelvin": TemperatureConverter.celsius_to_kelvin,
    "kelvin-to-celsius": TemperatureConverter.kelvin_to_celsius,
    "fahrenheit-to-kelvin": TemperatureConverter.fahrenheit_to_kelvin,
    "kelvin-to-fahrenheit": TemperatureConverter.kelvin_to_fahrenheit
}

# Dynamic endpoint creation
for route, func in conversion_functions.items():
    @app.get(f"/{route}")
    async def convert(value: float, func=func):
        result = func(value)
        return {"input": value, "output": result}
