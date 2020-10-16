def notas(*n, sit=False):
    """
    ->Avalia as notas de uma turma
    :param n: Digite as notas que deseja avaliar (podem ser quantas quiser)
    :param sit: atribua True se quiser saber a situação da turma
    :return: retorna um dicionário com o total, maior nota, menor nota e média.
    """
    dicionario = dict()
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    media = sum(n) / len(n)
    dicionario['media'] = media
    if sit:
        if media >= 7:
            dicionario['situação'] = 'BOA'
        elif 5 <= media < 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario


# Programa Principal
resp = notas(8, 9, 9, 9, 0, sit=True)
print(resp)