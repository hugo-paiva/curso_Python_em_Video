from datetime import date
born = int(input('Qual é o seu ano de nascimento? '))
today = int(date.today().year)
idade = today - born
alistamento = born + 18
print('Quem nasceu em {} tem {} anos em {}.'.format(born, idade, today))
if idade<18:
    print('Faltam {} anos para você se alistar.'.format(18-idade))
elif idade == 18:
    print('Você deve procurar a junta militar para se alistar.')
    print('Seu alistamento será em {}'.format(alistamento))
elif idade>18:
#else: apresenta o mesmo resultado
    print('Você já passou {} anos da idade de alistamento.'.format(idade-18))
    print('Seu alistamento foi em {}.'.format(alistamento))
