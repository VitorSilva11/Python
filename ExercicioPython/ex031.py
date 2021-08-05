from random import randint
from time import sleep

print("*=" * 20)
print("\tGerador De Número Mega Sena")
print("*=" * 20)

lista = []
jogos = []

qnt_jogo = int(input("Quantos Jogos Você Deseja Sortear: "))


for cont in range(0, qnt_jogo):
    x = 0
    while(True):
        numero = randint(0, 60)
        if(numero not in lista):
            lista.append(numero)
            x += 1
            if(x >= 6):
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print("-=" * 3, f"Sorteando {qnt_jogo} Jogos", "-=" * 3)

for indice, valor in enumerate(jogos):
    print(f"Jogo {indice + 1} - {valor}")
    sleep(1)

print("$" * 5, "-> BOA SORTE <- ", "$" * 5)