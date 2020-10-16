inicio = int(input('Digite o primeiro termo da sua Progressão Aritmética: '))
razao = int(input('Digite a razão da PA: '))
pa = inicio
termos = 0
cont = 1
mais = 10
while mais != 0:
    termos = termos + mais
    while cont <= termos:
        print('{}'.format(pa), end=' => ')
        pa = pa + razao
        cont += 1
    print('PAUSE')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print('='*35)
print('Foram apresentados {} termos da sua Progressão Aritmética.'.format(termos))
print('Programa encerrado com sucesso! Até mais!')
