import json

file = open('weather.json','r')
print(file.read())

weather = file.read()
weather = json.loads(weather)
print(weather['main']['temp'])
print(weather['weather'][0]['icon'])

