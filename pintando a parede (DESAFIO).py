largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
print('Sua parede tem dimensões de {}x{}'.format(largura, altura))


a = largura*altura
tinta = a / 2

print('A aréa é de {}m²'.format(a))
print('Será necessário {}l de tinta'.format(tinta))
