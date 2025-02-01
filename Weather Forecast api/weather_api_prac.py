import requests
import time

def forecast_write(date,city,temp,condition):
    filename = "Weather Forecast api\\Weather forecast data.txt"
    with open(filename,'a') as file:
        file.write(f"\nDate - {date}, City - {city}, Temperature - {temp}, Condition - {condition}")
        time.sleep(0.2)
    
def clear_data():
    filename = "Weather Forecast api\\Weather forecast data.txt"
    with open(filename,'w') as file:
        file.write("")

def get_weather_forecast(city_name, api_key='3ab817b814da587b58f0254154ff38db'):
    url = f'https://samples.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    r = requests.get(url)

    data = r.json()
    forecasts = data['list']  

    for forecast in forecasts:  # Iterate over the list properly
        main = forecast['main']
        weather = forecast['weather'][0]  # Access the first element of the weather list

        forecast_write(forecast['dt_txt'],city_name, main['temp'],weather['description'])
        
# Test the function
action = input("Get weather forecast (get) / Clear history (clear) -")
if (action.lower()=="get"):
    city_name = input("Enter the city name -")
    get_weather_forecast(city_name)

else:
    clear_data()
