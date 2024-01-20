def make_name(obj):
    return obj['name'] + ', ' + obj['region'] + ', ' + obj['country']


def get_default_location():
    return ''


def set_default_location(place):
    return ''


def formatted_info(data):
    current = data['current']

    return f"""
{make_name(data['location'])}    
- Temperature: {current['temp_c']}°C
- Condition: {current['condition']['text']}
- Wind: {current['wind_dir']} at {current['wind_kph']} kph
- Humidity: {current['humidity']}%
- UV Index: {current['uv']}
    """
