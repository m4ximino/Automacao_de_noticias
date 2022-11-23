import requests
from bs4 import BeautifulSoup

def get_http(url):
    try:
         return requests.get(url)
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
				requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(str(e))
    except Exception as e:
        raise

def get_noticias(content):
    soup = BeautifulSoup(content, 'lxml')
    noticias = soup.find_all('li', {'class':'latest__news__live__item'})
    lista_noticias = []
    for noticia in noticias:
        info_noticia = noticia.find('h3').string
        lista_noticias.append(info_noticia)
    return lista_noticias

if __name__ == '__main__':
    url = 'https://www.cnnbrasil.com.br/ao-vivo/'

    r = get_http(url)
    if r:
        lista_noticias = get_noticias(r.text)
        cont = 0
        for noticia in lista_noticias: 
            cont+=1
            print(cont,"--",noticia)