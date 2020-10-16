def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: O valor do Fatorial de um número num
    """
    f = 1
    print('-' * 30)
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


# Programa Principal
print(fatorial(4))
help(fatorial)
