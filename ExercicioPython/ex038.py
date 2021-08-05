
def calcularArea(c,l):
    area = l * c
    print(f"A área de um terreno {c:.1f}x{l:.1f} é de {area:.1f}m²")


print("Calcular Área")
print("-" * 10)

comprimento = float(input("Digite o comprimento: "))
largura = float(input("Digite a largura: "))

calcularArea(largura, comprimento)
