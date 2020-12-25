def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar os dados.\033[m')
            continue
        except:
            print('\033[0;31mERRO! Por favor digite um número inteiro válido.\033[m')
            return 0
        else:
            return valor


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc