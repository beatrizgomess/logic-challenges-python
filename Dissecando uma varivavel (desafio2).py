# Dissecando uma variável

n = input('Digite algo: ')
# y = input('Digite mais uma vez: ')
# x = input('Mais uma: ')
print('O tipo primitivo desse valor é: ', type(n))
# print('Este é:', type(y))
# print('E por último, este é:', type(x))

print('Só tem espaços? ', n.isspace())
print('Só tem número?', n.isnumeric())
print('É alfabetico?', n.isalpha())
print('É alfanúmerico? ', n.isalnum())
print('Está em maiuscúlo?', n.isupper())
print('Está em minuscúlo?', n.islower())
print('Está Capitalizada?', n.istitle())