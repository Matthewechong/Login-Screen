import requests
from pprint import pprint

def weather_data(query):
	res = requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=****************************8&units=metric');
	return res.json()

def print_weather(result,city):
	print("{}'s temperature: {} Celsius".format(city,result['main']['temp']))

