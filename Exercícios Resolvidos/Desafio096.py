def area(a, b):
    area = a * b
    print(f'A área de um terreno de {a}x{b} é de {area:.2f}m².')


# Programa Principal
print(f'{"Controle de Terrenos":^40}')
print('-' * 40)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
