import requests
import json

r = requests.get('https://api.adviceslip.com/advice')

conselho = json.loads(r.text)

conselho = conselho['slip']['advice']

print('CONSELHO DO DIA: ', conselho)    