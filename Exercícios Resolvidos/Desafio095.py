jogador = dict()
tabela = list()
while True:
    print('-' * 60)
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gols = []
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols fez na {c}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    tabela.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [N/S]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 40)
print(tabela)
print('-=' * 40)
