import requests


session = requests.Session()

url = 'http://www.maisbolao.com.br'
response = session.get(url)
response.text.find('Meus Bolões')

email = SEU_EMAIL
senha = SUA_SENHA

params = {'Email': email
          'Senha': senha}


response = session.post(url, params=params)
print(response.text.find('Meus Bolões'))
