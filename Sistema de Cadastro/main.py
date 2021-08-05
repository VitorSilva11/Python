from time import sleep
from modulos.interface import*
from modulos.arquivo import*

arq = 'pessoasCadastradas.txt'
arq2 = 'produtos.txt'


while True:
    resposta = menu(['Ver Funcionario Cadastrados', 'Cadastrar Nova Pessoa', 'Ver Produtos Cadastrados', 'Cadastrar Novo Produto', 'Sair do Sistema'])

    if resposta == 1:
        lerArquivoPessoa(arq)
        sleep(1.5)
    elif resposta == 2:

        cabecalho('Novo Cadastro')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
        sleep(1.5)
    elif resposta == 3:
        lerArquivoProduto(arq2)
        sleep(1.5)

    elif resposta == 4:
        cabecalho('Novo Cadastro')
        nome = input('Nome: ')
        preco = leiaFloat('Preço: ')
        cadastrarProduto(arq2, nome, preco)

    elif resposta == 5:
        cabecalho('Saindo do Sistema - Até Logo- ')
        break
    else:
        print('\033[31m[Error!]\033[m')
        sleep(2)