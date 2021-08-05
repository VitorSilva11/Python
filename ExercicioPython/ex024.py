
#implimentando o método sorth

lista = []

for cont in range(0, 5):
    numero = int(input("Digite um número: "))

    if(cont == 0 or numero > lista[-1]):
        lista.append(numero)
        print("Número adicionado no final da lista")

    else:
        posicao = 0
        while posicao < len(lista):
            if(numero < lista[posicao]):
                lista.insert(posicao, numero)
                print(f"Número adiciona na posição {posicao}...")
                break

            posicao += 1

print("!=" * 30)

print(lista)

print(lista)



