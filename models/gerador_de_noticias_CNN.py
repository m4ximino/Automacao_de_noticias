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

def get_noticias_CNN(content):
    soup = BeautifulSoup(content, 'lxml')
    noticias = soup.find_all('li', {'class':'latest__news__live__item'})
    lista_noticias = []
    cont=0
    for noticia in noticias:
        cont+=1
        info_noticia = [cont,noticia.find('h3').string, noticia.find('a').get('href')]
        lista_noticias.append(info_noticia)
    return lista_noticias

def get_noticia_completa_CNN(content):
    soup = BeautifulSoup(content, 'lxml')
    reportagem = soup.find_all('div', class_= 'post__content')
    tbody = []
    for temp in reportagem:
        for t_temp in temp.find_all('p'):
            if t_temp.string != None:
                tbody.append(t_temp.string)
    return ' '.join(tbody)


# if __name__ == '__main__':
#     url = 'https://www.cnnbrasil.com.br/ao-vivo/'

#     # r = get_http(url)
#     # if r:
#     #     lista_noticias = get_noticias(r.text)
#     #     cont = 0
#     #     for noticia in lista_noticias: 
#     #         print(noticia[1])
#     ex = 'https://www.cnnbrasil.com.br/esporte/richarlison-se-solidariza-com-vitimas-de-ataque-a-tiros-no-espirito-santo/'
#     r = get_http(ex)
#     if ex:
#         reportagem = get_noticia_completa(r.text)
#         print(reportagem)