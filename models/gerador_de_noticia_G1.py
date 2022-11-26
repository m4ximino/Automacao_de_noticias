import requests
from bs4 import BeautifulSoup

def get_noticias_G1(content):
    soup = BeautifulSoup(content, 'lxml')
    noticias = soup.find_all('a', {'class':'feed-post-link gui-color-primary gui-color-hover'})
    lista_noticias = []
    cont=0
    for noticia in noticias:
        cont+=1
        info_noticia = [cont,noticia.string, noticia.get('href')]
        lista_noticias.append(info_noticia)
    return lista_noticias


url = 'https://g1.globo.com/'
r = requests.get(url)

print(get_noticias_G1(r.text))