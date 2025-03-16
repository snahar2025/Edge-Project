import requests

# Get your API key from OpenWeatherMap
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    # Construct the full URL to request weather data
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    
    # Make the GET request to OpenWeatherMap API
    response = requests.get(complete_url)
    
    # Check if the response was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Extract necessary data
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        
        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found or invalid API key.")

# Main function to run the app
def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()