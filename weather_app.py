import requests
print('===| Check Current Weather Condition In Your City |===')
city = input('Enter City Name: ').capitalize()
api = requests.get(f'http://api.weatherapi.com/v1/current.json?key=afba79dd92b64ce8b68153056241801&q={city}&aqi=no')
data=api.json()

print(f'\n{city} Current Tempreature in Degree °C ->',data['current']['temp_c'])
print(f'\n{city} Current Tempreature Fahrenheit °F ->',data['current']['temp_f'])
print(f'\n{city} Current Weather Condition is ->',data['current']['condition']['text'])

print('\n','Thank You'.center(50,'='))
