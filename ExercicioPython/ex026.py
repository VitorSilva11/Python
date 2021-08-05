
lista = []
lista_pares = []
lista_impares = []

while(True):
    numero = int(input("Digite um Número: "))
    lista.append(numero)

    if(numero % 2 == 0):
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    continuar = str(input("Você deseja continuar[S/N]: ")).upper()
    if(continuar == "N"):
        break

print("!=" * 30)

print(f"Lista completa: {lista}")
print(f"Lista de Números Pares: {lista_pares}")
print(f"Lista de Números Impares: {lista_impares}")