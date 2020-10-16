print('{}'.format('10 TERMOS DE UMA PA'))
i = int(input('Digite o primeiro número da sua Progressão Aritmética: '))
razão = int(input('Digite a razão:'))
décimo = i + (10-1)*razão
for c in range(i, décimo+1, razão):
   print(c, end=' => ')
print('Acabou!')
