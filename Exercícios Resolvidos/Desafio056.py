somaidade = 0
maior = 0
menoridade = 0
velho = ''
for p in range(1, 4):
    print('====== {}ª PESSOA ======'.format(p))
    nome = str(input('Digite o nome: ')).strip().lower()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    somaidade = somaidade + idade
    if p == 1 and sexo == 'M':
        maior = idade
        velho = nome
    if p > 1 and sexo == 'M':
        if idade > maior:
            maior = idade
            velho = nome
    if sexo == 'F' and idade < 20:
        menoridade += 1
média = somaidade/4
print('A média de idade do grupo é {} anos.'.format(média))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, velho.capitalize()))
print('O número de mulheres com menos de 20 anos é {}'.format(menoridade))
