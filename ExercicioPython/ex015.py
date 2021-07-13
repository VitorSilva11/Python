print('----' * 10)
print('\tAlugel De Carro')
print('----' * 10)

dias = int(input('Digite Quantos Dias Você Ficou Com O Carro: '))
km = float(input('Digite Quantos Kilometros Rodados: '))

pagar = (dias * 60) + (km * 0.15)

print('O Preço Que Você Pagara Por {} Dias E {} KM Rodados Será De: {:.2}'.format(dias, km, pagar))
