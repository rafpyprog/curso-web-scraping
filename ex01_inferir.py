from bs4 import BeautifulSoup
import requests

# enviamos uma requisão HTTP utilizando o método GET
response = requests.get('http://www.inferir.com.br')
html = response.text

# realizamos o parse do HTML utilizando BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# buscamos a imagem utilizando a tag e a classe 
# encontradas na Ferramenta de Desenvolvedor
classe_logo = 'logo-mobile scale-with-grid'
logo_inferir = soup.find('img', {'class': classe_logo})
print(logo_inferir)

url = logo_inferir['src']

with open('logoinferir.png', 'wb') as f:
    f.write(requests.get(url).content)
