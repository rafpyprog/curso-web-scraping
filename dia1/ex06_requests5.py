''' Versão melhorada com data de corte dinâmica'''
from datetime import date
from concurrent.futures import ProcessPoolExecutor

import requests


def download_url(url, nome_arquivo):
    ''' Acessa a url utilizando o método HTTP GET, verifica o tipo de conteúdo e armazena no arquivo passado como parâmetro '''

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


if __name__ == '__main__':
    '''
    Fundos de Investimento: Documentos: Informe Diário
    http://dados.cvm.gov.br/dataset/fi-doc-inf_diario
    O INFORME DIÁRIO é um demonstrativo que contém as seguintes informações do
    fundo, relativas à data de competência:
        * Valor total da carteira do fundo;
        * Patrimônio líquido;
        * Valor da cota;
        * Captações realizadas no dia;
        * Resgates pagos no dia;
        * Número de cotistas
    '''

    today = date.today()
    print('Data atual:', today)

    url = 'http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{ano}{mes}.csv'
    for ano in (2017, 2018):
        for mes in range(1, 12 + 1):
            url_csv = url.format(ano=ano, mes=str(mes).zfill(2))
            print(url_csv)
            # utilizamos o nome do arquivo csv da url
            arquivo_saida = url_csv.split('/')[-1]
            download_url(url_csv, arquivo_saida)
            # encerra o loop no último informativo disponível
            if ano == today.year and mes == today.month:
                print('Downloads realizados com sucesso.')
                break
