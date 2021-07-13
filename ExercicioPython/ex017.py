from math import pow, sqrt

Cateto_Oposto = float(input('Digite O Cateto Oposto: '))
Cateto_Adjacente = float(input('Digite O Cateto Adjacente: '))

hipotenuza = pow(Cateto_Oposto, 2) + pow(Cateto_Adjacente, 2)

print('A Hipotenuza Será {:.2f}'.format(sqrt(hipotenuza)))

