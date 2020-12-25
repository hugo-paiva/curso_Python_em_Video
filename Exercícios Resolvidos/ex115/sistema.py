from ex115.lib.arquivo import *
from ex115.lib.interface import *
from time import sleep

arq = 'listaDoHugo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de ler o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de mostrar o conteúdo do arquivo
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
