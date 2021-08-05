
lista = []

while(True):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    continuar = str(input("Você deseja continuar[S/N]: ")).upper()
    if (continuar == "N"):
        break

print("!=" * 30)

print(f"Foi adicionado {len(lista)} elementos")

lista.sort(reverse = True)

print(lista)

if 5 in lista:
    print("O número 5 está na lista!")
else:
    print("O número 5 não está na lista!")

