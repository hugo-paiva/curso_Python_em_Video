import wget


site = 'http://www.pudim.com.br/'
try:
    result = wget.download(site)
    print(f'O site {site} encontra-se disponível.')
except:
    print(f'O site {site} encontra-se \033[0;31mindisponível.\033[m')
finally:
    print('Obrigado, volte sempre!')
