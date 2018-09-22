from multiprocessing import Process, Pool
import re
import sys
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent



def extract_urls(html):
    ''' Extrai as urls de um HTML, exclui as ocorrências duplicadas
    e retorna uma lista com os resultados '''
    
    soup = BeautifulSoup(html, 'html.parser')
    urls = set(a['href'] for a in soup.select('a[href]') if a['href'])    
    return list(urls)


def is_valid_url(url):    
    VALID_URL_PATTERN = '^https?.*'
    starts_with_http = re.match(VALID_URL_PATTERN, url) is not None    
    is_not_internal_reference = urlparse(url).fragment == ''
    return starts_with_http and is_not_internal_reference
    

def normalize_url(url, current_url):
    if url[0] == '/' or url.startswith('..'):
        url = urljoin(current_url, url)                
    return url.lower().strip()


def is_domain_url(url, domain):
    WWW = '^www\.'
    url_domain = urlparse(url).netloc
    if re.match(WWW, url_domain):
        url_domain = url_domain[4:]

    if re.match(WWW, domain):
        domain = domain[4:]
    
    return url_domain == domain or url_domain.endswith(domain) 
    

def request_data(url, verify=True):
    headers = {'User-Agent': generate_user_agent()}
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.SSLError:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.ConnectionError:
        return url, None
    #response.raise_for_status()
    print(f'Crawled {url}')
    return url, response


def extract_data(url):
    _, response = request_data(url)
    if response is not None:
        url_list = extract_urls(response.content)
        return url, url_list
    else:
        return url, []


def crawl_web(initial_url, ignore=None, pool_size=8):
    counter = 0
    domain = urlparse(initial_url).netloc
    print('Dominio:', domain)

    crawled, to_crawl = [], []
    to_crawl.append(initial_url)

    counter = 0
    while to_crawl:        
        with Pool(pool_size) as p:
            responses = p.map(extract_data, to_crawl)        
        to_crawl = []

        for current_url, url_list in responses:
            crawled.append(current_url)            
            for n, url in enumerate(url_list, 1):
                url = normalize_url(url, current_url)

                if re.match(ignore, url):
                    continue
                
                if is_valid_url(url) and is_domain_url(url, domain):
                    if url not in crawled and url not in to_crawl:                    
                        to_crawl.append(url)                
        print(f'{len(to_crawl)} links to crawl. Crawled: {counter}')
    return crawled


if __name__ == '__main__':
    url = sys.argv[1]
    crawl_web(url, ignore='.*\.(pdf|jpg|gif|png|exe|pkg|zip)$')
