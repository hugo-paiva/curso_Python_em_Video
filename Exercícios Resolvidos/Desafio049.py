n = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for c in range(0,10+1):
    print('{} x {:2} = {}'.format(n,c,n*c))
print('-'*12)