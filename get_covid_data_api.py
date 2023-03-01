import requests as rqs
import json
import jsonlines as jsl

# Dados de Covid do Mundo
covid_mundo_response = rqs.get('https://covid19-brazil-api.now.sh/api/report/v1/countries')
covid_dados_mundo = covid_mundo_response.json()

print('Mundo Response Status: ' + f'{covid_mundo_response.status_code}')

with jsl.open('covid_dados_mundo.jsonl', 'w') as writer:
    writer.write_all(covid_dados_mundo['data'])

# Dados de Covid dos Estados do Brasil
covid_brasil_response = rqs.get('https://covid19-brazil-api.now.sh/api/report/v1')
covid_dados_brasil = covid_brasil_response.json()

print('Brasil Response Status: ' + f'{covid_brasil_response.status_code}')

with jsl.open('covid_dados_brasil.jsonl', 'w') as writer:
    writer.write_all(covid_dados_brasil['data'])