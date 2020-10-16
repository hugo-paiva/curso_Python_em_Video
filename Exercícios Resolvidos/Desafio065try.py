resp = 'S'
soma = quant = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma = soma + n
    quant = quant + 1
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / quant
print('Foram digitados {} valores e a média é {}.'.format(quant, media))
print('O menor valor digitado foi {} e maior foi {}.'.format(menor, maior))
