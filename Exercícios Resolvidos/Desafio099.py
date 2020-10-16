from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1.5)
    cont = mai = 0
    for v in num:
        print(f'{v} ', end='')
        sleep(0.5)
        if v == num[0]:
            mai = v
        else:
            if v > mai:
                mai = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior número foi {mai}.')


# Programa Principal
maior(8, 10, 3, 9)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
