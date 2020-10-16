frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A primeira ocorrência da letra "a" é na posição {}'.format(frase.find('a')+1))
print('A última ocorrência da letra "a" é na posição {}'.format(frase.rfind('a')+1))
