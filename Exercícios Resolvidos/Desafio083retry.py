expressao = str(input('Digite uma expressão matemática: '))
pilha = []
for simbol in expressao:
    if simbol == '(':
        pilha.append('(')
    elif simbol == ')':
        if len(pilha) > 0:
            pilha.pop()
        elif len(pilha) == 0:
            pilha.append(')')
if len(pilha) > 0:
    print('Sua expressão não é válida.')
elif len(pilha) == 0:
    print('Sua expressão é válida')
