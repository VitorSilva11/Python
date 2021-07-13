 ##Modulo para utilizar números aleatorios

import random

##Gerando número Aleatorio
numero_secreto = random.randrange(1, 101)


#Criando a pontuação do jogo

pontuacao = 1000

##Escolhendo a dificuldade do jogo


dificuldade = int(input("Escolha a difilcudade do jogo: (1) Fácil  (2)Médio  (3)Difício\n-- "))

while(dificuldade > 3 or dificuldade < 1):

    dificuldade = int(input("Digite um número válido: "))

if(dificuldade == 1):
    tentativa = 20

elif(dificuldade == 2):
    tentativa = 10

else:
    tentativa = 5


print("#################################################")
print("----- ", "Bem Vindo ao Jogo de Adivinhação ", "-----")
print("-----", "Tentativas: ", tentativa, " -----")
print("#################################################")


   ## Pegando o número do usuario

chute = int(input("Digite um Número: "))

   ## Comparando os números

while(tentativa > 1 and chute > 0 and chute <= 100):



 ## Verificando se o usuario acertou o número secreto

    if(chute > numero_secreto):
        tentativa -= 1

        print("\n\n\n\n\n\n")
        print("*************************")
        print("Tentativas: ", tentativa)
        print("*************************")
        print("Você Errou!!")

        pontuacao = pontuacao - (abs(numero_secreto - chute))

        print("***************************************************")
        print("Dica: O seu chute foi maior que o número secreto.")
        print("***************************************************")

        chute = int(input("Digite um novo número: "))
        print("\n\n\n\n\n\n")
    elif(chute < numero_secreto):
        tentativa -= 1

        print("\n\n\n\n\n\n")
        print("*************************")
        print("Tentativas: ", tentativa)
        print("*************************")
        print("Você Errou!!")

        pontuacao = pontuacao - (abs(numero_secreto - chute))

        print("*************************************************")
        print("Dica: O seu chute foi menor que o número secreto.")
        print("***************************************************")

        chute = int(input("Digite um novo número: "))
    else:
        print("\n\n\n\n\n\n")
        print("********************************")
        print("-- Parabenss!!! Você Acertoou --")
        print("********************************")
        break

print("--------------------")
print(" Sua Pontuação: {} ".format(pontuacao))

