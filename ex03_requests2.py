import requests

url = "https://www.python.org/static/img/python-logo.png"
response = requests.get(url)
print('Response:', response)

print('Status Code:', response.status_code)

print('Headers:', response.headers)

'''O campo Content-Type do cabeçalho nos mostra que o servidor retornou uma
imagem no formato png, cujo  tamanho é 45.187 bytes de acordo com o campo
Content-Length.'''

'''Agora que confirmamos estas informações, podemos salvar a
imagem em um arquivo, utilizando o conteúdo binário da resposta obtido
através da propriedade content'''
arquivo_destino = 'logo-python.png'
with open(arquivo_destino, 'wb') as pngfile:
    pngfile.write(response.content)
