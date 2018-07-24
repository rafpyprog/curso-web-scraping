'''
Curso de Web Scraping com Python
desafio_login_testing_groud.py - Web Scraper Testing Ground
Instruções: http://testing-ground.scraping.pro/login
'''
import requests


sesssion = requests.Session()

login_url = 'http://testing-ground.scraping.pro/login'
data = {'usr': 'admin', 'pwd': 12345}
response = sesssion.post(login_url, data=data)
response.raise_for_status()

LOGIN_OK = 'WELCOME :)'
if LOGIN_OK in response.text:
    print('Login realizado com sucesso.')
else:
    print('Falha no login')
