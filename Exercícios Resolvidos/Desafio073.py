brasileirao = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Corinthias',
               'Flamengo', 'Atlético Minerio', 'Athletico Paranaense',
               'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo',
               'Fluminense', 'Vasco da Gama', 'Bahia', 'Sport', 'Vitória',
               'Ponte Preta', 'América', 'Coritiba')
print('-='*30)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*30)
print(f'Os 5 primeiros são {brasileirao[:5]}')
print('-='*30)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*30)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição.')