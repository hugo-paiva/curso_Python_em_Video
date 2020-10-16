from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for v in range(0, 5):
        temp = randint(1, 10)
        lista.append(temp)
        print(f'{temp} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(list):
    soma = 0
    for v in list:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {list}, temos {soma}')


# Programa Principal
valores = list()
sorteia(valores)
somaPar(valores)
