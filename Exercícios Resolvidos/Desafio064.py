n = soma = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma = soma + n
        cont = cont + 1
print('Ao final da operação foram somados {} números com resultado {}'.format(cont, soma))