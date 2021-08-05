
jogador = dict()
time = []

while(True):
    jogador.clear()
    jogador['nome'] = input("Nome do Jogador: ")
    jogador['gols'] = []
    jogador['total'] = 0
    qnt_partidas = int(input('Quantas Partidas Você Jogou: '))

    for cont in range(0, qnt_partidas):
        jogador['gols'].append(int(input(f'Digite a quantidade de gols do {cont + 1} Jogo: ')))
        jogador['total'] += jogador['gols'][cont]

    time.append(jogador.copy())
    continuar = input("[S/N]Você Deseja Continuar: ").upper()
    if(continuar != 'S' and continuar != 'N'):
        while(True):
            print("[Erro!]Digite Apenas [S] ou [N]")
            continuar = input("[S/N]Você Deseja Continuar: ").upper()
            if continuar == 'N':
                break
            elif continuar == 'S':
                break
    if(continuar == 'N'):
        break



print("=!" * 30)
print(f'{"Cod.":<5} {"Nome":<15} {"Gols":<15} {"Total"}')
print("-" * 40)

for i,j in enumerate(time):
    print(f'{i:<5}', end='')
    for valor in j.values():
        print(f'{str(valor):<15}', end='')
    print()

print("-" * 40)

while(True):
    exebir = int(input("[999 Para Encerrar] Digite o código do jogador: "))
    while(True):
        if(exebir >= len(time) or exebir < 0):
            print(f'[Error!]Código {exebir} Não existe.')
            exebir = int(input("[999 Para Encerrar] Digite o código do jogador: "))
            if(exebir == 999):
                break
        if(exebir >= 0 and exebir < len(time)):
            break

    if(exebir == 999):
        break

    print(f"=== Levantamento De Gols Do Jogador {time[exebir]['nome']} ===")
    for cont in range(0, len(time[exebir]['gols'])):
        print(f'Jogo {cont + 1} Marcou {time[exebir]["gols"][cont]} gols')



