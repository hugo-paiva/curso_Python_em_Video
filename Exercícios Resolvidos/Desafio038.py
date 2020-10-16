a = int(input('\033[31mDigite um número: \033[m'))
b = int(input('\033[4;33mDigite outro: \033[m'))
if a>b:
    print('O \033[31mprimeiro valor\033[m é maior.')
elif b>a:
    print('\033[4;33mO segundo valor é maior\033[m')
else:
    print('Não existe valor maior, os dois são iguais.')