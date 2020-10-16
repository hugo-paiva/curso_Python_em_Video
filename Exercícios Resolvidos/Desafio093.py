ficha = dict()
ficha['jogador'] = str(input('Nome do jogador: ')).title().strip()
partidas = int(input(f'Quantas partidas {ficha["jogador"]} jogou: '))
gols = []
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols fez na {c}ª partida? ')))
ficha['gols'] = gols[:]
ficha['total'] = sum(gols)
print('-=' * 40)
print(ficha)
print('-=' * 40)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {ficha["jogador"]} jogou {len(ficha["gols"])} partidas ')
for p, g in enumerate(ficha['gols']):
    print(f'  => Na partida {p + 1}, fez {g} gols')
print(f'Foi um total de {ficha["total"]} gols')
