from time import sleep
operação = 0
num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
while operação != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    operação = int(input('Escolha uma operação acima: '))
    if operação == 1:
        soma = num + num2
        print('A soma de {} e {} é {}'.format(num, num2, soma))
    elif operação == 2:
        multiplicação = num * num2
        print('O produto de {} e {} é {}'.format(num, num2, multiplicação))
    elif operação == 3:
        maior = num
        if num < num2:
            maior = num2
        print('O maior valor é {}'.format(maior))
    elif operação == 4:
        print('Informe os números novamente:')
        num = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif operação == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida! Tente novamente')
    print('=-='*10)
    sleep(2)
print('FIM. Até mais!')
