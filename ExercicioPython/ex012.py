print('----' * 15)
print('\tCalculo De Desconto')
print('----' * 15)

salario = float(input('Digite O Seu Salário: '))
porcentagem = float(input('Digite A Porcentagem De Desconto: '))

desconto = salario * porcentagem / 100

print('Com o Desconto de {} O Salário ficara: {:.2f}'.format(porcentagem, salario - desconto))


