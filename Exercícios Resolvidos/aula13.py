'''s = 0
for c in range(0,4):
    n = int(input('Digite um número:'))
    #s = s + n
    s += n
print('O somatório dos valores foi {}'.format(s))'''

frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.split()
join = ''.join(frase)
inverso = ''
for letras in range(len(join)-1, -1, -1):
    inverso = inverso + join[letras]
print('Você digitou {} cujo inverso é {}'.format(join, inverso))
if join == inverso:
    print('Logo é palindromo')
else:
    print('Portanto não é palíndromo.')

