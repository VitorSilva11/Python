# O arquivo principal que vai rodar, onde nele vai poder escolher qual jogo o usuario vai desejar jogar.
#--------------------------------------------------------------------------------------------------------
# Importando os jogos da forca e adivinhação

import adivinhacao
import forca

print("***************************")
print("\tEscolha o Seu Jogo  ")
print("***************************")

sair = 1

while(sair == 1):
    print("\n(0)Não jogar -  (1) Jogo da Adivinhação - (2) Jogo da Forca")

    jogo = int(input("Selecione o Seu Jogo: "))

    if(jogo == 1):
        print("\n\t***** Você Selecionou o Jogo da Adivinhação *****\n")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("\n\t***** Você Selecionou o Jogo Da Forca *****\n")
        forca.jogar()
    elif(jogo == 0):
        print("\n\t==== Volte Sempre!!!! ====")
        sair = 0

    else:
        print("\n(0)Não jogar -  (1) Jogo da Adivinhação - (2) Jogo da Forca")
        jogo = int(input("-- Você precisa selecionar uma opção: "))