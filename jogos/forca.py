##Criando o jogo da forca

#importando a biblioteca que gera numeros aleatorios

import random

##Função onde vai ser utlizada para executar o jogo no arquivo principal jogos

def jogar():
    print("***********************")
    print("\tJogo Da Forca ")
    print("\tDica: Fruta")
    print("***********************")


#abrindo o arquivo que tem as palavras do jogo
    arquivo = open("palavra.txt", "r") #utilizando o modo de leitura que o paranmetro 'r'
#lendo as palavras do arquivo e armazenando
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

#fechando o arquivo
    arquivo.close()

#Criando palavra chave

    numero = random.randrange(0, len(palavras))
    palavra_chave = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_chave]

    tentivas = 0


    print(letras_acertadas, "\n")

    se_enforcou = False
    acertou = False

    ## Enquando não se_enforcou e não acertou. Rode novamente

    while(not se_enforcou and not acertou):

        chute = input("Chute uma Letra: ").strip().upper()
        index = 0

        if(chute in palavra_chave):
            index = 0
            for letra in palavra_chave:
                if(chute == letra):
                    letras_acertadas[index] = letra

                index += 1

        else:
            tentivas += 1
            desenha_forca(tentivas)


        print(letras_acertadas)
        acertou = "_" not in letras_acertadas
        se_enforcou = tentivas == 7

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_chave)


#Analisando se o jogo for executado direto sem utilizar o arquivo jogos, ele vai conseguir rodar.
if(__name__ == "__main__"):

    def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    def imprime_mensagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


    def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if(erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    jogar()