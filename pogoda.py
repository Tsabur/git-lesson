import pyowm

city = input('Введите город: ')

owm = pyowm.OWM('6a4c1768e1c1a1a709a3bcd61bfe756d', language="ru")
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print('В городе ' + city + ' сейчас: ' + str(temperature) + '°С')
print('Также в городе ' + city + ' сейчас ' + w.get_detailed_status())

