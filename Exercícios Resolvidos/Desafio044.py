print('\033[1;46m{:=^40}\033[m'.format(' LOJAS HUGO '))
normal = float(input('Qual é o valor das suas compras? R$'))
condição = int(input('''FORMAS DE PAGAMENTO:
[ 1 ] à vista no dinheiro
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?'''))
if condição ==1:
    p = normal*.9
    print('À vista no dinheiro o valor cai de R${:.2f} para R${:.2f} com 10% de desconto.'.format(normal, p))
elif condição ==2:
    p = normal*.95
    print('À vista no cartão o valor cai de R${:.2f} para R${:.2f} com 5% de desconto.'.format(normal, p))
elif condição ==3:
    p = normal
    print('Em até 2x no cartão o preço é o mesmo de R${:.2f}'.format(p))
elif condição ==4:
    p = normal*1.2
    totparc = int(input('Quantas parcelas?'))
    parcela = p/totparc
    print('Sua compra será efetuada em {} parcelas de R${}'.format(totparc, parcela))
    print('Em 3x ou mais no cartão o valor passa de R${:.2f} para R${:.2f} com 20% de juros.'.format(normal, p))
else:
    print('Opção inválida. Tente novamente.')