import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_description = weather['description']
        
        weather_report = (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Pressure: {pressure} hPa\n"
            f"Description: {weather_description}"
        )
        
        return weather_report
    else:
        return "City not found or API request failed."

if __name__ == "__main__":
    api_key = "2a7c13d4c3e808edfee52512ef14bff4"
    city = input("Enter city name: ")
    print(get_weather(api_key, city))
