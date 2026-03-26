import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant information from the API response
            main_data = data['main']
            temperature = main_data['temp']
            humidity = main_data['humidity']
            description = data['weather'][0]['description']

            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description}")
        else:
            print(f"Error {response.status_code}: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY" ##"ENTER_YOUR_OPENWEATHERMAP_API_KEY"
    city = input("Enter the city name: ")
    get_weather(api_key, city)
