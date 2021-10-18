import json

# file = open('weather.json','r')
# #print(file.read())
#
# weather = file.read()
# weather = json.loads(weather)
# print(weather['main']['temp'])
# print(weather['weather'][0]['icon'])

print('\n--------------練習-----------------')

file = open('weather.json','r')
data = file.read()
weather = json.loads(data)