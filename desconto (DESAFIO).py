p = float(input('Digite um valor'))
print('Seu produto custa {}: '.format(p))
x = float(input('Seu desconto é de: %'))
desconto = (p*x) / 100
nv = p - desconto
print('Seu desconto é de R${}'.format(desconto))
print('Valor Original {}'.format(p))
print('Novo valor (Com desconto) {}'.format(nv))



