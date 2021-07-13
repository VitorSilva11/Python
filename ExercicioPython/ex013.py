print('---' * 15)
print('\tCalculando O Reajuste')
print('---' * 15)

salario = float(input('Digite O Valor Do Seu Salário: '))
aumento = float(input('Digite A Porcentagem De Aumento: '))

reajuste = salario * (aumento + 100) / 100

print('Com A Porcentagem De Aumento De - {}, O Salário Ficara R${:.2f} '.format(aumento, reajuste))
