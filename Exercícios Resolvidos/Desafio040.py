sair = False
while sair == False:
    a = float(input('Entre com a primeira nota: '))
    b = float(input('Entre com a segunda nota: '))
    media = (a+b)/2
    print('Sua média foi de {:.1f}'.format(media))
    if media<5:
        print('\033[0;31mREPROVADO\033[m')
    elif 5<=media<7:
        print('\033[32mRECUPERAÇÃO\033[m')
    else:
        print('\033[36mAPROVADO\033[m')
    fim = str(input('Deseja sair?(s/n)'))
    if fim == 's':
        sair = True

