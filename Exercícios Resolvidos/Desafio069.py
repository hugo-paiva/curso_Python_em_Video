maioridade = quantho = menormulher = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        quantho += 1
    if sexo == 'F' and idade < 20:
        menormulher += 1
    continuar = ' '
    print('-'*30)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('='*30)
print('Programa encerrado.')
print('-'*30)
print(f'Ao todo {maioridade} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {quantho} homens.')
print(f'{menormulher} mulheres tem menos de 20 anos.')