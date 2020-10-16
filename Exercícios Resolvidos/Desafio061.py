'''inicio = int(input('Digite o primeiro número da PA:'))
razão = int(input('Digite a razão da PA: '))
enesimo = razão*(10 - 1) + inicio
print('A progressão aritmética de {} com razão {} é:'.format(inicio, razão))
for num in range(inicio, enesimo +1, razão):
    print('{}'.format(num), end=' => ')
print('Fim.')'''

inicio = int(input('Digite o primeiro termo da sua Progressão Aritmética: '))
razão = int(input('Digite a razão: '))
pa = inicio
cont = 1
termos = 0
mais = 10
while mais > 0:
    termos = termos + mais
    while cont <= termos:
        print('{}'.format(pa), end=' => ')
        pa += razão
        cont += 1
    print('PAUSADO!')
    mais = int(input('Gostaria de ver mais quantos termos? '))
print('Programa encerrado com sucesso! Foram mostrados {} termos da PA.'.format(termos))