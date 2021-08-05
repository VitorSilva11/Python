from datetime import datetime

def eleicao(idade):
    if idade < 18 and idade >= 16:
        return 'Voto Opcional!'
    elif(idade >= 18):
        return 'Voto Obrigatorio!'
    else:
        return 'Não Pode Votar!'



anoNascimento = int(input('Digite sua data de nascimento: '))
idade = datetime.now().year - anoNascimento

print(f"Com {idade}: {eleicao(idade)}")
