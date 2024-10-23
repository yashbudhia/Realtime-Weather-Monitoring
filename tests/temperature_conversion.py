from weather.processor import kelvin_to_celsius

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(300) == 26.85  # Example conversion
    assert kelvin_to_celsius(273.15) == 0  # Freezing point
    assert kelvin_to_celsius(373.15) == 100  # Boiling point
