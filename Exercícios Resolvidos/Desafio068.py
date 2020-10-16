print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
from random import randint
cont = 0
while True:
    print('-=' * 30)
    pc = randint(1, 100)
    player = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = pc + player
    resto = soma % 2
    if resto == 0:
        resultado = 'PAR'
    if resto == 1:
        resultado = 'IMPAR'
    print(f'Você jogou {player} e o computador {pc}. Total de {soma} DEU {resultado}')
    print('-' * 30)
    if escolha == 'P':
        if resto == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    if escolha != 'P':
        if resto != 0:
            print('Você venceu!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('Você perdeu!')
            break
print(f'Você acertou {cont} partidas consecutivas!')



