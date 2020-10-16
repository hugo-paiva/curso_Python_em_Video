from random import randint
lista = []
jogos = []
deseja = int(input('Quantos jogos você deseja fazer? '))
quant = 1
while quant <= deseja:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    quant += 1
print(jogos)







'''from random import randint
from time import sleep
jogo = [0, 0, 0, 0, 0, 0]
temp = 0
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
totjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {totjogos}  JOGOS -=-=-=')
for c in range(1, totjogos + 1):
    for num in range(0, 6):
        temp = randint(1, 60)
        if temp not in jogo:
            jogo[num] = temp
    print(f'Jogo {c}: {sorted(jogo)}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')'''