'''frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ','')
reverso = frase
reversed(reverso)
print('O inverso de \033[4;36m{}\033[m é {}'.format(frase, reverso))
if frase == reverso:
    print('Esta sentença é um palíndromo')
else:
    print('\033[31mEsta sentenção NÃO é palíndromo.')'''

#
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if frase == inverso:
    print('Temos um Palíndromo.')
else:
    print('Esta sentenção NÃO É palíndroma.')