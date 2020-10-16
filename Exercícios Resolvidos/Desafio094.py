pessoa = {}
lista = list()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M] ')).upper().strip()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO. Digite apenas F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if resp in 'Nn':
        break
print('-' * 60)
print(f' - Foram cadastradas {len(lista)} pessoas.')
media = soma / len(lista)
print(f' - A média de idade do grupo é {media}')
print(f' - A todo as mulheres são: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print(f'\n - Ao todo estes homens estão acima da idade média de {media} anos: ')
for p in lista:
    if p['idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('=' * 60)
print(f'{"<<<<  VOLTE SEMPRE  >>>>":^60}')
print('=' * 60)
