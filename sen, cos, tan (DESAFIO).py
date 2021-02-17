'''co = float(input('Cateto oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = float(input('Hipotenusa: '))

sen = co/hi
cos = ca/hi
tan = co/ca
print('As medias dos ângulos são: ')
print('Seno = '.format(sen))
print('Cosseno = '.format(cos))
print('Tangente = '.format(tan))'''
import math # fom math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você quer: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Suas medidas são - seno {:.2f}, cos {:.2f} e tan {:.2f}'.format(seno, cos, tan))
