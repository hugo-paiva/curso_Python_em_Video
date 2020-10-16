n = int(input('Digite um número qualquer: '))
resto = n % 2
if resto == 0:
    print('\033[4;33mSeu número é par!\033[m')
else:
    print('\033[4;31mSeu número é impar!\033[m')