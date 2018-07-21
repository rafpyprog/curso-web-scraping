import requests


def download_url(url, nome_arquivo):
    ''' Acessa a url utilizando o método HTTP GET, verifica o tipo de conteúdo
    e armazena no arquivo passado como parâmetro '''

    response = requests.get(url)
    response.raise_for_status()

    content_type = response.headers.get('Content-Type', '')

    if content_type.startswith('text'):
        mode = 'w'  # escrita de arquivo texto
        dados = response.text
    else:
        mode = 'wb'  # escrita de arquivo binário
        dados = response.content

    with open(nome_arquivo, mode) as f:
        f.write(dados)

    msg = ('Download do conteúdo {} da url {} armazenado '
           'com sucesso no arquivo {}.')
    print(msg.format(content_type, url, nome_arquivo))

    return response
