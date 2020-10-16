inicio = int(input('Digite o primeiro termo da sua PA? '))
razão = int(input('Digite um número: '))
pa = inicio
cont = 1
termos = 0
mais = 10
while mais != 0:
    termos += mais
    while cont <= termos:
        print('{}'.format(pa), end=' => ')
        pa = pa + razão
        cont += 1
    mais = int(input('Deseja mostrar mais termos? '))
print('FIM')