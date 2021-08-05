from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
rank = []

for cont in range(0,4):
    dado = randint(1, 6)
    jogadores[f"Jogador{cont + 1}"] = dado

print("Valores Sorteados")

for chave, valor in jogadores.items():
    print(f"O {chave} Tirou {valor} no Dado")
    sleep(1)


print("!=" * 30)
#Deixar em ordem o dicionario
rank = sorted(jogadores.items(), key = itemgetter(1), reverse=True)


for indice, valor in enumerate(rank):
    print(f"{indice + 1} - {valor[0]} com o número {valor[1]}")
    sleep(1)


