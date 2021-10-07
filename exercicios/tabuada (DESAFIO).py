x = int(input('Digite um número para saber a tabuada: '))
print('-' * 12)
aux = 0
print('A tabuada de {} é '.format(x))
while (aux <= 10):
    print('{0} X {1} = {2}'.format(x, aux, (aux * x)))
    aux = aux+1
print('-' * 12)