print('='*20, ' {} '.format('ANALISADOR DE NÚMEROS'), '='*20 )
soma = 0
cont = 1
sair = False
n = int(input('Digite um número: '))
soma += n
maior = menor = n
while sair == False:
    exit = str(input('Deseja sair? [s/n] ')).strip().lower()
    if exit == 's':
        sair = True
    else:
        n = int(input('Digite um número: '))
        soma += n
        cont += 1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/cont
print('='*40)
print('A média entre todos os valores foi {}'.format(media))
print('O menor valor digitado foi {} e o maior foi {}'.format(menor, maior))
