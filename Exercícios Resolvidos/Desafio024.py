'''cidade = input('Digite o nome da cidade: ').strip().lower()
s = cidade.split()
primeiro = s[0]
if primeiro == 'santo':
    print('Sua cidade começa com "santo"')
else:
    print('Sua cidade começa com outro nome.')'''

#ou pelo método
cid = str(input('Digite o nome da cidade: ')).strip().lower()
print(cid[:5] == 'santo')