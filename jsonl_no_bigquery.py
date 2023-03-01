import json
from google.cloud import bigquery
from google.oauth2 import service_account

with open('chave_bigquery.json', 'r') as Reader:
    chave_bigquery_dict = json.load(Reader)

credentials = service_account.Credentials.from_service_account_info(chave_bigquery_dict)
client = bigquery.Client(credentials=credentials)

def upload_dados_jsonl(nome_arquivo):
    table_id = f'wide-exchanger-367908.Covid_Dados.{nome_arquivo}'  

    job_config = bigquery.LoadJobConfig(source_format='NEWLINE_DELIMITED_JSON',
        autodetect=True
    )

    with open(f'{nome_arquivo}.jsonl', 'rb') as reader:
        job = client.load_table_from_file(file_obj=reader,
            destination=table_id,
            job_config=job_config)
        job.result()

def dropar_tabelas_bigquery():
    query = """
        DROP TABLE Covid_Dados.covid_dados_mundo;
        DROP TABLE Covid_Dados.covid_dados_brasil;
        DROP TABLE Covid_Dados.covid_vacinacoes_brasil;
    """
    job = client.query(query=query)

dropar_tabelas_bigquery()
upload_dados_jsonl('covid_dados_brasil')
upload_dados_jsonl('covid_dados_mundo')
upload_dados_jsonl('covid_vacinacoes_brasil')