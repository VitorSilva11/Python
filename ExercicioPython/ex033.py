aluno = dict()

aluno['Nome'] = input("Nome: ")
aluno['Media'] = float(input(f"Digite a sua média {aluno['Nome']}: "))

if(aluno['Media'] < 7 and aluno['Media'] > 4):
    aluno['Situacao'] = 'Recuperação'
elif(aluno['Media'] < 4):
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Aprovado'

for chave, valor in aluno.items():
    print(f"{chave} é = {valor}")


