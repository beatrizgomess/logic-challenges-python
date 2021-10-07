
'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hp = (co**2 + ca**2) ** (1/2)
print('A hipotenusa vale {:.2f}'.format(hp))
'''
import math #from math import hypot (PARA CÁLCULO DE HIPOTENUSA)
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))

