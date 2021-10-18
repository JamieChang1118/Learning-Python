import json
import requests


url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=4549f1be0f4a49c9c04f0bc7d615be19'
# 從網路上抓下來的
weather = requests.get(url).text
weather = json.loads(weather)
print(weather)

temp = weather['main']['temp']
icon = weather['weather'][0]['icon']

temp = float(temp) - 237.15

print(temp)
print(icon)

icon_url = 'https://openweathermap.org/img/wn/' + icon + '@2x.png'
print(icon_url)
icon_data = requests.get(icon_url).content

# file = open('weather_icon.png' , 'wb')
# file.write(icon_data)

with open('weather_icon.png' , 'wb') as file:
    file.write(icon_data)


