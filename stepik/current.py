import requests
import json

url = 'http://numbersapi.com/'

# numbers = input().split('\n')
result = []
params = {'Content-Type': 'json', 'type' : 'math'}
# print(numbers)
with open('1.txt', 'r') as file:
    x = file.read()
    for i in x.split():
        r = requests.get(url + i + '/math/'+'?json')
        # print(r.text)
        data = r.json()
        if data['found'] != False:
            print('Interesting')
        else:
            print('Boring')

