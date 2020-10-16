expressao = str(input('Digite um expressão matemática: '))
parentesis = []
for v in expressao:
    if v == '(' or v == ')':
        parentesis.append(v)
metade1 = []
metade2 = []
if len(parentesis) % 2 == 0:
    for c in range(0, int(len(parentesis) / 2)):
        metade1.append(parentesis[c])
    for c in range(int(len(parentesis) / 2), len(parentesis)):
        if parentesis[c] == ')':
            metade2.append('(')
    if metade1 == metade2:
        print('Sua expressão é válida.')
    else:
        print('Esta expressão não é válida.')
else:
    print('Esta expressão não é válida')
print(metade1)
print(metade2)