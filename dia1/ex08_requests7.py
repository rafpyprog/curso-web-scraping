'''
Curso de Webscraping com Python
ex08_requests7.py - API Banco Central
Documentação da API: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/swagger-ui3#/
'''

import csv
import json

import requests


base_url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url = base_url + 'Moedas'
print('Acessando:', url)
response = requests.get(url)

# formato JSON
print('Content-Type:', response.headers['Content-Type'])

dados = json.loads(response.content)
print(dados)

campos = dados['value'][0].keys()
print(campos)

# salvando os dados em um arquivo csv
nome_arquivo = 'moedas.csv'
with open(nome_arquivo, 'w', newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    for i in dados['value']:
        writer.writerow(i)
