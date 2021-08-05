from datetime import datetime

cadastro = dict()

cadastro['nome'] = input("Nome: ")
ano_nascimento = int(input("Ano de Nascimento: "))
cadastro['idade'] = datetime.now().year - ano_nascimento


cadastro['ctps'] = int(input("[0 - Não tem]Carteira de Trabalho: "))


if cadastro['ctps'] == 0:
    print("!=" * 30)
    for key, valor in cadastro.items():
        print(f'{key} - {valor}')

else:
    print("!=" * 30)
    cadastro['contratacao'] = int(input("Digite o ano de contratação: "))
    cadastro['salario'] = float(input("Digite o seu Salário R$:"))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - datetime.now().year)

    for key, valor in cadastro.items():
        print(f'{key} - {valor}')