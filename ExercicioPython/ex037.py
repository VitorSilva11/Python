
pessoa = {}
lista = []
somaIdade = 0

while(True):
    pessoa.clear()
    pessoa['nome'] = input("Nome: ")

    pessoa['idade'] = int(input("Idade: "))
    if(pessoa['idade'] < 0):
        while(True):
            pessoa['idade'] = int(input("[Erro!]Digite uma idade Válida: "))
            if (pessoa['idade'] > 0):
                break

    somaIdade += pessoa['idade']

    pessoa['sexo'] = input("Sexo[M/F]: ").upper()

    if(pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F'):
        while(True):
            pessoa['sexo'] = input("[Erro!]Digite [M] ou [F]").upper()
            if(pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F'):
                break

    lista.append(pessoa.copy())
    continuar = input("[S/N]Deseja Continuar: ").upper()
    if(continuar != 'S' and continuar != 'N'):
        while(True):
            continuar = input("[Erro!]Digite [S] ou [N]").upper()
            if continuar == 'N':
                break
            elif continuar == 'S':
                break
    if(continuar == 'N'):
        break

print("-=" * 30)

print(f"Quantidade de Pessoas Cadastradas: {len(lista)}")
mediaIdade = somaIdade / len(lista)
print(f'A Média de idade é {mediaIdade:.0f}')
print(f'As Mulheres Cadastradas Foram:', end='')

for p in lista:
    if(p['sexo'] == 'F'):
        print(f'[{p["nome"]}]', end=' ')


print("\nLista de Pessoas Acima da Média de idade")
for p in lista:
    if(p['idade'] > mediaIdade):
        for key, valor in p.items():
            print(f"{key} = {valor} - ", end=" ")
        print()
