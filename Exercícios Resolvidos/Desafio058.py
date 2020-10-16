from random import randint
print('Olá, sou seu computador!')
pc = randint(0, 10)
player = int(input('Tente adivinhar o número que escolhi de 0 a 10: '))
palpites = 0
while player != pc:
    palpites += 1
    if player > pc:
        print('Menos...')
    else:
        print('Mais...')
    player = int(input('Tente novamente: '))
print('Parabéns! Você acertou o número que pensei foi {}!'.format(pc))
print('E você usou {} palpites.'.format(palpites))

