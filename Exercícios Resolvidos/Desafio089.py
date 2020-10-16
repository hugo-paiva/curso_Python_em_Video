princ = []
while True:
    nome = str(input('Nome: ')).title().strip()
    num1 = float(input('Nota 1: '))
    num2 = float(input('Nota 2: '))
    media = (num1 + num2) / 2
    princ.append([nome, [num1, num2], media])
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":<8}')
print('-' * 30)
for i, p in enumerate(princ):
    print(f'{i:<5}{p[0]:<15}{p[2]:<8.1f}')
print('-' * 40)
while True:
    p = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe): '))
    if p == 999:
        print('FINALIZANDO...')
        break
    if p <= len(princ) - 1:
        print(f'Notas de {princ[p][0]} são {princ[p][1]}')
print('<<< VOLTE SEMPRE >>>')

