import random

aluno1 = str(input('Digite O Nome Do Primeiro Aluno: '))
aluno2 = str(input('Digite O Nome Do Segundo Aluno: '))
aluno3 = str(input('Digite O Nome Do Terceiro Aluno:'))
aluno4 = str(input('Digite O Nome Do Quarto Aluno:'))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('A Ordem De Apresentação Será: \n',lista)
