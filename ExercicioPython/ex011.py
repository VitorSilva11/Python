
print('------' * 10)
print('Descobrindo Quantos Litros De Tintas Você Precisa Para Pintar Sua Parede')
print('------' * 10, '\n\n')

altura = float(input('Digite A Altura Da Sua Parede: '))
largura = float(input('Digite A Largura Da Sua Parede: '))

area = largura * altura
Litros_Tinta = area / 2

print('Sua Parede Tem a Dimensão {} X {}, Sua Área é {}'.format(largura, altura, area))
print('Você Precisara De {} Litros De Tinta'.format(Litros_Tinta))

