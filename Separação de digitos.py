numero = int(input("Digite um número de 0 a 9999: "))
n = str(numero)
print("Milhar: {}".format(n[0]))
print("Centena: {}".format(n[1]))
print("Dezena: {}".format(n[2]))
print("Unidade: {}".format(n[3]))


# Outra Forma - ENTENDER O CALCÚLO DE MCDU
print("=" * 10)
U = numero // 1 % 10
D = numero // 10 % 10
C = numero // 100 % 10
M = numero // 1000 % 10
print(": {}".format(U))
print("Centena: {}".format(D))
print("Dezena: {}".format(C))
print("Unidade: {}".format(M))





