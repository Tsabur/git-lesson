import pyowm

city = input('Введите город: ')

owm = pyowm.OWM('6a4c1768e1c1a1a709a3bcd61bfe756d', language="ru")
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print('In the city ' + city + ' now: ' + str(temperature) + '°С')
print('And in the city ' + city + ' now ' + w.get_detailed_status())


fc1 = owm .three_hours_forecast ( city )
f = fc1.get_forecast()
for weather in f:
    print (weather.get_reference_time('iso'), weather.get_status(), weather.get_temperature(unit='celsius'))

