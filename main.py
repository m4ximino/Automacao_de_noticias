from time import sleep
import models.gerador_de_noticias_CNN

def main() -> None:
    menu()


def menu() -> None:
    print('===================================')
    print('========== Bem-vindo(a) ===========')
    print('====== Gerador_de_Noticias  =======')
    print('===================================')

    print('Selecione uma opção abaixo: ')
    print('1 - CNN Brasil')
    print('2 - G1 Globo')
    print('3 - UOL')
    print('4 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        get_CNN()
    elif opcao == 2:
        get_G1()
    elif opcao == 3:
        get_UOL()
    elif opcao == 4:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def get_CNN():
    url = 'https://www.cnnbrasil.com.br/ao-vivo/'
    r = models.gerador_de_noticias_CNN.get_http(url)
    if r:
        print('Selecione uma opção abaixo para ler a matéria completa: ')
        list_not = models.gerador_de_noticias_CNN.get_noticias_CNN(r.text)
        for nti in list_not: print(nti[0], '-', nti[1])
        opcao: int = int(input())
        for nti in list_not: 
            if opcao == int(nti[0]):
                url = nti[2]
                r = models.gerador_de_noticias_CNN.get_http(url)
                if r:
                    print('MATÉRIA COMPLETA:')
                    reportagem = models.gerador_de_noticias_CNN.get_noticia_completa_CNN(r.text)
                    print(reportagem)
            # else: 
            #     print('Opção invalida!')
            #     get_CNN()
    sleep(1)
    print('Selecione uma opção abaixo: ')
    print('1 - Ler outra matéria')
    print('2 - Menu')
    opcao: int = int(input())
    if opcao == 1: get_CNN()
    else: menu()
    

def get_G1():
    None

def get_UOL():
    None

if __name__ == '__main__':
    main()