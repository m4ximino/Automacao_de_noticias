import requests
from bs4 import BeautifulSoup

def get_pegar_noticia(content):
    soup = BeautifulSoup(content, 'lxml')
    noticias = soup.find_all('i', {'class':'col-sm-22 col-md-22 col-lg-22 custom-title'})
    for noticia in noticias:
        return noticia.string

def get_noticias_UOL(content):
    soup = BeautifulSoup(content, 'lxml')
    noticias = soup.find_all('a', {'class':'hyperlink headlineSub__link'})
    lista_noticias = []
    cont=0
    for noticia in noticias:
        r = requests.get(noticia.get('href')).text
        if get_pegar_noticia(r) != None:
            cont+=1
            info_noticia = [cont,get_pegar_noticia(r), noticia.get('href')]
            lista_noticias.append(info_noticia)
    return lista_noticias

def get_noticia_completa_UOL(content):
    soup = BeautifulSoup(content, 'lxml')
    reportagem = soup.find_all('p', class_= 'content-text__container')
    tbody = []
    for temp in reportagem:
        for t_temp in temp:
            tbody.append(t_temp.string)
    return ''.join(tbody)

# url = 'https://www.uol.com.br/'
# r = requests.get(url)
# print(get_noticias_UOL(r.text))
# <h3 id="lazbz114" class="title__element headlineSub__content__title">
# <h3 class="thumb-title title-xsmall title-lg-small title-xs-medium">'Também perco uma mãe', lamenta filha de homem morto escondido em freezer</h3>
# <a href="https://www.uol.com.br/esporte/futebol/copa-do-mundo/2022/11/27/otimismo-sobre-neymar-aumenta-e-jogo-contra-a-suica-decidira-estrategia.htm" class="hyperlink headlineSub__link">flex
# <i class="col-sm-22 col-md-22 col-lg-22 custom-title" ia-title>Otimismo sobre Neymar aumenta, e jogo contra a Suíça decidirá estratégia </i>