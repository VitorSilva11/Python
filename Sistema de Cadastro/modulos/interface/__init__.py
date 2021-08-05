def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[Error]Digite um número inteiro válido: \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m[Error!]Digite um número: \033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[Error]Digite um valor válido: \033[m')

        except KeyboardInterrupt:
            print('\033[31m[Error!]Digite um valor: \033[m')
            continue
        else:
            return n

def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'\033[36m{txt.center(42)}\033[m')
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    cont = 1
    for item in lista:
        print(f'\033[32m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opcao = leiaInt('\033[35mSua Opção: \033[m')
    return opcao
