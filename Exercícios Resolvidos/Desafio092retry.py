from random import randint
from operator import itemgetter

dados = dict()
print('Valores sorteados')
for j in range(1, 5):
    dados[f'jogador{j}'] = randint(1, 6)
for k, v in dados.items():
    print(f'  {k} tirou {v}')
print(dados)
ranking = dict()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(dados):
    print(f' {i + 1}º lugar:  {v} com {