import requests


def download_url(url, outfile='downloadfile.data'):
    response = requests.get(url)
    response.raise_for_status()
    tipo = response.headers['Content-Type']

    if tipo.startswith('text'):
        mode = 'w'
        data = response.text
    else:
        mode = 'wb'
        data = response.content

    with open(outfile, mode) as f:
        f.write(data)

    return tipo
