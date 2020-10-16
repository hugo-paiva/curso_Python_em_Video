print('-=='*20)
print('Analisador de triângulos')
print('-=='*20)
a = int(input('\033[33mQual o valor de a?\033[m'))
b = int(input('\033[4;31mQual o valor de b ?\033[m'))
c = int(input('\033[7;37;40mQual o valor de c?\033[m'))
'''if abs(b-c)<a<b+c:
    if abs(a-c)<b<a+c:
        if abs(a-b)<c<a+b:
            print('{}, {} e {} formam um triangulo'.format(a, b, c))
        else:
            print('nao rola')
    else:
        print('nao rola')
else:
    print('nao rola')'''

# ou de maneira simplificada
if a < b+c and b<a+c and c<a+b:
    print('Os segmentos de tamanho {}, {} e {} FORMAM um triângulo!'.format(a, b, c))
else:
    print('Estes segmentos não formam um triângulo.')