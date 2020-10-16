'''def leiaInt(msg):
    valor = str(input(msg)).strip()
    while not valor.isnumeric():
        print('\033[031mERRO! Digite um número interiro válido.\033[m')
        valor = str(input(msg))
    valor = int(valor)
    return valor'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor



# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
