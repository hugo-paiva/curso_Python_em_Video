aluno = dict()
aluno['nome'] = str(input('Digite seu nome: ')).title().strip()
aluno['Média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['Média'] >=7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f' -- {k} é igual a {v}')