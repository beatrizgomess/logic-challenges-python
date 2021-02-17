x = int(input('Digite o valor em reais: '))

d = (x * 5.29)
e = (x * 6.39)
i = (x * 0.051)

print('O valor em dolár é US${:2}'.format(d))
print('O valor em euros é {}'.format(e))
print('O valor em ienes (Moeda Japonesa) é {}'.format(i))
