from weather.api import get_weather_data

def test_get_weather_data():
    weather_data = get_weather_data('Delhi')
    assert weather_data is not None
    assert 'main' in weather_data
    assert 'temp' in weather_data['main']
