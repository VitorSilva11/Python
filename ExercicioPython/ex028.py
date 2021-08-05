
dados = []
pessoas = []
maior = 0
menor = 99999
total_pessoas = 0

def cadastro():
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite seu peso: ")))
    pessoas.append(dados[:])
    dados.clear()

while(True):
    cadastro()
    if(maior < pessoas[total_pessoas][1]):
        maior = pessoas[total_pessoas][1]
    elif(menor > pessoas[total_pessoas][1]):
        menor = pessoas[total_pessoas][1]

    total_pessoas += 1
    continuar = str(input("Deseja Continuar [S/N]: ")).upper()
    if(continuar == "N"):
        break

print("*=" * 30)

print(f"Total de Pessoas Cadastrada: {total_pessoas}")

print(f"O maior peso cadastrado foi {maior}.KG", end="")
for people in pessoas:
    if(people[1] == maior):
        print(f"[{people[0]}] ", end="")

##############################################################
print("")

print(f"O menor peso cadastrado foi {menor}.KG", end="")
for people in pessoas:
    if(people[1] == menor):
        print(f"[{people[0]}] ", end="")

