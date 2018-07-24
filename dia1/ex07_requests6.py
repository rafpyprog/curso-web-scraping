'''
Web Scraping com Python - Requests
ex07_requests6.py - Pesquisa no Wimoveis
'''

import requests


session = requests.Session()

url = 'https://www.wimoveis.com.br/'
response = session.get(url)
response.raise_for_status()
print('Status code (GET):', response.status_code)

pagina_carregou = response.text.find('Encontre o imóvel dos seus sonhos') != -1
if pagina_carregou:
    print('Página carregou com sucesso.')
else:
    print('Erro no carregamento da página.')
    raise


# parametros de consulta descobertos com o Dev Tools
params = {
    'idCiudad': '',
    'idProvincia': '',
    'idSubZona': '',
    'idZonaDeValor': '',
    'tipoDeOperacion': 1,
    'tipoDePropiedad': 2,
    'tipoHomeCookie': '',
    'ubicacion': 'aguas claras'
    }

# cabeçalhos para que o servidor aceite a requisição
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
           'Host': 'www.wimoveis.com.br',
           'Referer': 'https://www.wimoveis.com.br/'}

# envia os dados do formulário de consulta
url_post = 'https://www.wimoveis.com.br/listado.bum'
response = session.post(url_post, params=params, headers=headers)
print('Status code (POST):', response.status_code)

# validamos o resultado da consulta
QUANTIDADE_IMOVEIS = '7.389'
assert QUANTIDADE_IMOVEIS in response.text
