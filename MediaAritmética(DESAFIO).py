n1 = float(input('Digite a 1º nota'))
n2 = float(input('Digite a 2º nota'))
n3 = float(input('Digite a 3º nota'))
n4 = float(input('Digite a 4º nota'))

Resultado = (n1 + n2 + n3 + n4)/4
print('Sua média é {:.1f}'.format(Resultado))
if Resultado >= 7 :
    print('APROVADO')
else :
    print('REPROVADO')