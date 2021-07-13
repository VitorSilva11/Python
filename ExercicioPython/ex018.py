import math

angulo = float(input('Digite O Valor Do Ângulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangete = math.tan(math.radians(angulo))

print('O Seno Do Ângulo {} É: {:.2f}'.format(angulo, seno))
print('O Cosseno Do Ângulo {} é: {:.2f}'.format(angulo, cosseno))
print('A Tangete Do Ângulo {} é: {:.2f}'.format(angulo, tangete))


