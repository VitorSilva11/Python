
lista_num = []


while(True):
    auxiliar = True
    number = int(input("Digite um número: "))
    if( not number in lista_num):
        lista_num.append(number)
        print("Número adicionado com sucesso!")
        resposta = input("Deseja continuar S/N ?").upper()
        auxiliar = False

    if(auxiliar):
        print("Você Não pode Adicionar números Iguais!")
        resposta = input("Deseja continuar S/N? ").upper()

    if(resposta == "N"):
        break


print("~=" * 30)
lista_num.sort()
print(lista_num)




