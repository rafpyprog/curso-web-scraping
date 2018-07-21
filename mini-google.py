import requests
import re

def crawl_web(initial_url):
    crawled, to_crawl = [], []
    to_crawl.append(initial_url)

    while to_crawl:
        current_url = to_crawl.pop(0)
        print('|' + current_url + '|')
        r = requests.get(current_url)
        crawled.append(current_url)
        for url in re.findall('<a href="([^"]+)">', str(r.content)):
            if url[0] == '/':
                url = current_url + url
            pattern = re.compile('https?')
            if pattern.match(url) and url not in crawled:
                to_crawl.append(url)
    return crawled


crawl_web('https://www.fullstackpython.com/')
