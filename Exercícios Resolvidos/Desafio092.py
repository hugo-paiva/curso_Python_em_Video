from datetime import datetime
hoje = datetime.today().year
ficha = dict()
ficha['nome'] = str(input('Nome: ')).title().strip()
nasc = int(input('Ano de nascimento: '))
ficha['idade'] = hoje - nasc
ficha['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contração: '))
    ficha['salário'] = int(input('Salário: R$'))
    ficha['aposentadoria'] = 35 + ficha['contratação'] - nasc
print("-=" * 40)
for k, v in ficha.items():
    print(f'  --- {k} tem o valor {v}')
