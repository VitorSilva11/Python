
numeros = [[], []]

for cont in range(0, 7):
  dado =  int(input(f"Digite o {cont + 1} Número: "))

  if(dado % 2 == 0):
      numeros[0].append(dado)
  else:
      numeros[1].append(dado)


numeros[1].sort()
numeros[0].sort()

print(f"Números Pares: {numeros[0]}")
print(f"Números Ímpares: {numeros[1]}")

