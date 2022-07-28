
from email.charset import BASE64
from tempfile import tempdir
import requests

API_KEY = "38151216fb66391080df2a2503381acd"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:              # 200 means successfull response
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] -273.15)
    temperature_feels = round(data['main']['feels_like'] -273.15) 
    print ("Weather:", weather)
    print ("Temperature:", str(temperature) + "°C")
    print ("Apparent temperature:", str(temperature_feels) + "°C")
    
else:
    print("An error occurred. Probably city u lookin for does not exist in our database.")