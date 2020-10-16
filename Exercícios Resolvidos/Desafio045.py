from random import randint
from time import sleep
n = int(randint(1, 3))
player = int(input('''FAÇA SUA ESCOLHA
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Insira o número:'''))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if player == 1 and n ==1:
    print('EMPATE! Os dois escolheram pedra.')
if player ==1 and n ==2:
    print('Você perdeu! Você jogou PEDRA e eu PAPEL.')
if player ==1 and n ==3:
    print('PERDI. Você jogou PEDRA e eu TESOURA.')
if player ==2 and n==1:
    print('você ganhou papel enrola pedra!')
if player ==2 and n==2:
    print('EMPATE. nos dois jogamos papel.')
if player ==2 and n==3:
    print('Você perdeu! Tesoura corta papel.')
if player ==3 and n==1:
    print('Voce perdeu! Pedra quebra tesoura.')
if player==3 and n==2:
    print('okay você venceu! Tesoura corta papel.')
if player ==3 and n==3:
    print('TESOURADAS. Nós dois escolhemos tesoura.')

#VER RESOLUÇÃO DO GUANABARA
