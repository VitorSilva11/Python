import random

aluno1 = input('Digite O Nome Do Primeiro Aluno: ')
aluno2 = input('Digite O Nome Do Segundo Aluno: ')
aluno3 = input('Digite O Nome Do Terceiro Aluno: ')
aluno4 = input('Digite O Nome Do Quarto Aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
aleatorio = random.choice(lista)

print('O Aluno Escolhido Foi: {}'.format(aleatorio))
