# Criar uma lista, que o usuario digite 5 números e no final exiba o maior número e o menor número e sua posição


#criando a lista
lista = []
maior = 0
menor = 0


#estrutura de repetição para armazenar os valores digitado pelo usuario
for cont in range(0, 5):
    numero = input(f"Digite o número da posição [{cont}]: ")
    lista.append(numero)

 #Armazenando o maior e o menor número digitado
    if(cont == 0):
        maior = lista[cont]
        menor = lista[cont]
    else:
        if(maior < lista[cont]):
            maior = lista[cont]

        if(menor > lista[cont]):
            menor = lista[cont]

print("*=" * 30)


print(f"A lista que você digitou foi -- {lista} --")

print(f"O maior número digitado foi: -- {maior} --\n Nás posições: ", end="")
#saber qual posição está o maior número
for indice, valor in enumerate(lista):
    if(valor == maior):
        print(f"{indice}... ", end = "")

print()

print(f"O menor número digitado foi: -- {menor} --\n Nás posições: ", end="")
#saber qual posição está o menor número
for indece, valor in enumerate(lista):
    if(valor == menor):
        print(f"{indice}... ", end="")








