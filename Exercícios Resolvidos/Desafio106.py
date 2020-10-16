from time import sleep


def titulo(msg, n=0):
    if n != 0:
        print('\033', end='')
        if n == 1:
            print('[1;30;44m', end='')
        elif n == 2:
            print('[7;30m', end='')
        elif n == 3:
            print('[1;30;42m', end='')
        elif n == 4:
            print('[1;30;41m', end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    if n != 0:
        print('\033[m', end='')


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = input('Função ou biblioteca: ')
    if comando.upper().strip() == 'FIM':
        titulo('ATÉ LOGO', 4)
        sleep(2)
        break
    else:
        titulo(f'Acessando o manual do comando \"{comando}\"...', 1)
        sleep(1)
        print(f'\033[7;30m')
        help(comando)
        print('\033[m', end='')