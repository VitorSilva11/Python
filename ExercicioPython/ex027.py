
#Testando se a expressão está correta

expressao = str(input("Digite a sua expressão: "))
pilha = []

for simb in expressao:
    if (simb == "("):
        pilha.append("(")
    elif(simb == ")"):
       if(len(pilha)) > 0:
            pilha.pop()
       else:
           pilha.append(")")
           break

if(len(pilha) > 0):
    print("Expressão Válida!!!")
else:
    print("Expressão Inválida!!!")