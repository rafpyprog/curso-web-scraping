from inferir import download_url
import requests


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


    import os

    from datetime import date

    hoje = date.today()
    ano_dia = hoje.year
    mes_dia = hoje.month

    url = 'http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{ano}{mes}.csv'
    for ano in (2017, 2018):
        for mes in range(1, 12 + 1):
            url_csv = url.format(ano=ano, mes=str(mes).zfill(2))
            print(url_csv)
            ultimo = sorted(os.listdir())[-1]
            print('ulyimo', ultimo)
            print(url_csv.split('/')[-1][14:-4])
            if url_csv.split('/')[-1][:-4] > ultimo[13:-4]:
                # utilizamos o nome do arquivo csv da url
                arquivo_saida = url_csv.split('/')[-1]
                download_url(url_csv, arquivo_saida)
                # encerra o loop no último informativo disponível
            if ano == ano_dia and mes == mes_dia:
                break
