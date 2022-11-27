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

def get_noticia_completa_G1(content):
    soup = BeautifulSoup(content, 'lxml')
    reportagem = soup.find_all('p', class_= 'content-text__container')
    print(reportagem.string)
    # tbody = []
    # for temp in reportagem:
    #     for t_temp in temp.find_all('p'):
    #         tbody.append(t_temp.string)


url = 'https://g1.globo.com/es/espirito-santo/noticia/2022/11/26/pai-confirma-adolescente-baleada-aracruz.ghtml'
r = requests.get(url)
print(get_noticia_completa_G1(r.text))