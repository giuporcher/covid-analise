import requests as rqs
from requests.auth import HTTPBasicAuth
import json
import jsonlines as jsl
import re

vacinacao_response = rqs.post('https://imunizacao-es.saude.gov.br/_search?scroll=1m',
                    json={"size":10000},
                    auth= HTTPBasicAuth('imunizacao_public', 'qlto5t&7r_@+#Tlstigi'))

print('Vacinação Response Status: 'f'{vacinacao_response.status_code}')

vacinacao_json = vacinacao_response.json()
vacinacao_dados = vacinacao_json['hits']['hits']


for jsonl_obj in vacinacao_dados:
    covid_dados_dict = jsonl_obj['_source']

    for dict_key in list(covid_dados_dict):
        remover_arroba = re.sub('[@]', '', dict_key)
        covid_dados_dict[remover_arroba] = covid_dados_dict[dict_key]
        
        if bool(re.search(pattern='[@]', string=dict_key)):
            del covid_dados_dict[dict_key]
    

with jsl.open('covid_vacinacoes_brasil.jsonl', 'w') as writer:
    writer.write_all(vacinacao_dados)