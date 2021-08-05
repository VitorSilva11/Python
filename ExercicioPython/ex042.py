from random import randint
from time import sleep

def geradorNumeros(gerador):
    gerador = []
    for cont in range(0, 6):
        gerador.append(randint(1, 10))
    return gerador

def somarPares(lista):
    pares = 0

    for cont in lista:
        if cont % 2 == 0:
            pares += cont

    return pares

lista = []
lista = geradorNumeros(lista)
pares = somarPares(lista)

print("Gerando 5 Números: ", end='')
for cont in lista:
    print(f"{cont}", end=' ')
    sleep(0.5)
print(' -Pronto!-')

print(f"A Soma Dos Números Pares: -- {pares} --")


