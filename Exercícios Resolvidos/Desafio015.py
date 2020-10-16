dia = float(input('Quantos dias o carro esteve alugado? '))
rodado = float(input("Quantos quilômetros foram rodados? "))
total = dia*60 + rodado*0.15
print('Para {} dias e {} quilometros rodados o custo final é de R${:.2f}.'.format(dia, rodado, total))