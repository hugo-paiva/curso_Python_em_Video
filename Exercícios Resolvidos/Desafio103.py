def ficha(jogador='<desconhecido>', n=0):
    print(f'O jogador {jogador} fez {n} gol(s) no campeonato.')


print('-' * 30)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric() == False:
    gols = 0
if nome.strip() == '':
    ficha(n=gols)
else:
    ficha(nome, gols)
