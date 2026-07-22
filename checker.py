import requests 
import json

with open('data/data.json', 'r') as f:
    data = json.load(f)

name = input('Введите свой ник: ').strip()

for items in data:

    link = items['link']
    response = requests.get(f'{link}/{name}')

    if response.status_code == 200:
        print('Пользователь Найден')
    else:
        print('Пользователь Не Найден')


