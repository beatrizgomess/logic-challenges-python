km = float(input('Quantos km o carro pecorreu?'))
dias = float(input('Quantos dias ele permanceu alugado?'))
valorkm = km*0.15
valordia = dias*60
aluguel = valorkm + valordia
print('O total de km custa {}:'.format(valorkm))
print('O total de dias custa {}:'.format(valordia))
print('O aluguel custa {}'.format(aluguel))