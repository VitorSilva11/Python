from modulos.interface import  cabecalho

def arquivoExiste(nome):
    try:
        a = open('nome', 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivoProduto(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo')
    else:
        cabecalho('Produtos Cadastrados')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            dado[1] = dado[1].replace('.', ',')
            print(f'\033[32m{dado[0]:<30}\033[m\033[34mR${dado[1]:>3}\033[m')
    finally:
        a.close()


def lerArquivoPessoa(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo')

    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[32m{dado[0]:<30}\033[m\033[34m{dado[1]:>3} anos\033[m')

    finally:
        a.close()


def cadastrarProduto(arq, nome = 'desconhecido', preco = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{preco:.2f}')
        except:
            print('Houve um erro ao escrever no arquivo')
        else:
            print(f'Produto {nome} Cadastrado com Sucesso')
            a.close()

def cadastrarPessoa(arq, nome= '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')

    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever no arquivo')
        else:
            print(f'Registro de {nome} Cadastrado com Sucesso')
            a.close()