'''Create a weather application that:
Uses OpenWeatherMap API (free tier) OR wttr.in API
Takes city name as input
Displays:
  Current temperature
  Weather description
  Humidity
  Wind speed
Handles invalid city names
Allows checking multiple cities in a loop

Sample Output:
Enter city name: London
Weather in London:
Temperature: 15°C
Condition: Partly cloudy
Humidity: 72%
Wind: 12 km/h

Check another city? (yes/no):
'''
import requests
import json

API_KEY = "2d9deeb8d38588902fe0ee9dd27e503b"

def fetchDataFromApi(cityName, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {cityName}")
        print(f"Temperature: {data['main']['temp']} K")
        print(f"Condition: {data['weather'][0]['description']}") 
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} m/s")
        return True # Return True so the main loop can proceed
    elif response.status_code == 401:
        print("Error 401: Unauthorized.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
    return False

def main():
    while True:
        cityname = input("\nEnter city name: ")
        success = fetchDataFromApi(cityname, API_KEY)
        
        if success:
            checkAnother = input("Check another city? (yes/no):  ").lower()
            if checkAnother == "no":
                break
        else:
            print("Could not retrieve data for that city.")
            retry = input("Try again? (yes/no): ").lower()
            if retry == "no":
                break

if __name__ == "__main__":
    main()
