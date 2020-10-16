from random import randint
from time import sleep
from operator import itemgetter
sorteio = dict()
print('Valores sorteados:')
for c in range(1, 5):
    jogador = randint(1, 6)
    sorteio[f'jogador{c}'] = jogador
print(sorteio)
for k, v in sorteio.items():
    print(f'    {k} tirou {v} no dado.')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
