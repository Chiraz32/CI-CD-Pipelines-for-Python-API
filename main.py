class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

# Sample usage
if __name__ == "__main__":
    converter = TemperatureConverter()
    print("25°C to Fahrenheit:", converter.celsius_to_fahrenheit(25))
    print("77°F to Celsius:", converter.fahrenheit_to_celsius(77))
    print("0°C to Kelvin:", converter.celsius_to_kelvin(0))
    print("300K to Celsius:", converter.kelvin_to_celsius(300))
    print("32°F to Kelvin:", converter.fahrenheit_to_kelvin(32))
    print("300K to Fahrenheit:", converter.kelvin_to_fahrenheit(300))
