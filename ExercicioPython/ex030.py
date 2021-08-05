
matriz = [[], [], []]
soma_pares = 0
soma_3_coluna = 0
maior = 0

for coluna in range(0, len(matriz)):
    for linha in range(0, len(matriz)):
      matriz[coluna].append(int(input(f"Digite o valor na Coluna[{coluna}] e na Linha [{linha}]")))


print("-=" * 30)

for coluna in range(0, len(matriz)):
    for linha in range(0, len(matriz)):
        print(f"( {matriz[coluna][linha]:^5} )", end="")
        if(matriz[coluna][linha] % 2 == 0):
            soma_pares += matriz[coluna][linha]
    print()


for coluna in range(0, len(matriz)):
    soma_3_coluna += matriz[coluna][2]

for linha in range(0, len(matriz)):
    if(maior < matriz[1][linha]):
        maior = matriz[1][linha]

print("-=" * 30)

print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números da 3 Coluna: {soma_3_coluna}")
print(f"O maior número da 2 Coluna é: {maior}")