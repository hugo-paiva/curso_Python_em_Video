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


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar os dados.\033[m')
            return 0
        except:
            print('\033[0;31mERRO! O por favor digite um número real válido.\033[m')
            continue
        else:
            return valor


# Programa Principal
a = leiaInt('Digite um número inteiro: ')
b = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {a} e o número real {b}.')
