sair = False
while sair == False:
    print('='*15+' DESAFIO 13 '+'='*15)
    l = float(input('Qual é a largura da parede em metros? '))
    h = float(input('Qual é a altura da parede em metros? '))
    a = h*l

    # Cada litro de tinta pinta um área de 2m²
    t = a/2
    print('Para pintar uma parede de {} metros quadrados são necessários {} litros de tinta.'.format(a,t))
    conta =input('Deseja fazer outra conta?(s/n)')
    if conta == 'n':
        sair = True

