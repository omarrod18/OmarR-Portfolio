
import json
import requests

def handler(event, context):
    params = event['queryStringParameters']
    city = params.get('city', 'London')
    api_key = '2a7c13d4c3e808edfee52512ef14bff4'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] != 200:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'City not found'})
        }
    weather = {
        'city': city,
        'temperature': round(data['main']['temp'] - 273.15, 2),
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'description': data['weather'][0]['description']
    }
    return {
        'statusCode': 200,
        'body': json.dumps(weather)
    }
