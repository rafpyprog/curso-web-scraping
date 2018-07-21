import requests


session = requests.Session()

url = 'https://www.wimoveis.com.br/'
response = session.get(url)
print(response.status_code)
print(response.text)
siteok = response.text.find('Encontre o imóvel dos seus sonhos ')
print(siteok)

params = {
    'idCiudad': '',
    'idProvincia': '',
    'idSubZona': '',
    'idZonaDeValor': '',
    'tipoDeOperacion': 1,
    'tipoDePropiedad': 2,
    'tipoHomeCookie': '',
    'ubicacion': 'aguas+claras'
    }

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
           'Host': 'www.wimoveis.com.br',
           'Referer': 'https://www.wimoveis.com.br/'}
url_post = 'https://www.wimoveis.com.br/listado.bum'
response = session.post(url_post, params=params, headers=headers)
print(response.status_code)

assert '7.416' in response.text
