def voto(nasc):
    from datetime import datetime
    idade = datetime.today().year - nasc
    if idade >= 65:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: NÃO VOTA'


# Programa Principal
print('-' * 30)
nasc = int(input('Em que anos você nasceu? '))
print(voto(nasc))
