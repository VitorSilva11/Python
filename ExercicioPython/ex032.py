
lista = []
alunos = []


print("-=" * 20)
print("\tBOLETIM ESCOLAR")
print("-=" * 20)

while(True):
    lista.append(input("Digite O Nome: "))

    nota1 = float(input("Nota 1: "))
    lista.append(nota1)
    nota2 = float(input("Nota 2: "))
    lista.append(nota2)

    media = (nota1 + nota2) / 2
    lista.append(media)

    alunos.append(lista[:])
    lista.clear()

    continuar = input("Você Deseja Continuar[S/N]? ").upper()

    if continuar == "N":
        print("-" * 30)
        print(f'{"No":<4} {"Nome":<10} {"Média":>8}')
        print("-" * 30)
        for i,v in enumerate(alunos):
            print(f"{i:<4} {v[0]:<10} {v[3]:>8.1f}")
        print("-" * 30)
        break

while(True):
    exibir_nota = int(input("[999 Interrompe]Mostra Nota de Qual Aluno? "))
    if(exibir_nota == 999):
        break
    else:
        print(f"Notas de {alunos[exibir_nota][0]}: [Nota1: {alunos[exibir_nota][1]}] - [Nota2: {alunos[exibir_nota][2]}]")
        print("!=" * 30)

