import requests
import json

#custom written function to return weather info in a list
def get_weather_info():
   #base url for the API
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q=Tiruchirappalli&appid="
   API_KEY = " " #Enter your API key here
   URL = BASE_URL + API_KEY
   response = requests.get(URL)
   try:
      if response.status_code == 200:
         data = response.json()
         main = data['main']
         temperature = main['temp']
         temp_feel_like = main['feels_like']  
         humidity = main['humidity']
         pressure = main['pressure']
         weather_report = data['weather']
         wind_report = data['wind']
      result = []

      #converting the temprature from kelvin to celcius
      temperature_c = temperature - 273.15
      temp_feel_like_c = temp_feel_like - 273.15

      #appending the result to a list
      result.append(int(temperature_c))
      result.append(int(temp_feel_like_c))
      result.append(humidity)
      result.append(pressure)
      result.append(weather_report[0]['description'])
      result.append(wind_report['speed'])
      result.append(wind_report['deg'])
      return result
   except:
      print(Exception)
