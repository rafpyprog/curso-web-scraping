'''
Curso de Web Scraping com Python
ex02_requests1.py - Base de Dados do Comércio Exterior - MDIC
'''

import requests

url = 'http://www.mdic.gov.br/balanca/bd/ncm/EXP_2018.csv'

# envia uma requisição HTTP utilizando o método GET
response = requests.get(url)

''' acessa o texto da resposta enviada pelo servidor, seleciona a primeira linha
e imprime na tela '''
print(response.text.splitlines()[0])
