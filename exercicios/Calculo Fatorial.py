from math import factorial

print("=" * 40)
print("\t\tFATORIAL")
print("=" * 40)

n = int(input("Digite um numero: "))
fat = 1
i = n
print("Calculando {}! = ".format(n), end= '')
while i > 0:
    print("{}".format(i), end='')
    print(" x " if i > 1 else ' = ', end= '')
    fat *= i
    i = i - 1
    #print(fat)
print("\033[44m{}\033[m".format(fat))

print("FIM DO PROGRAMA")



fatorial = 1
n1 = int(input("DIGITE UM NÚMERO PARA SABER SEU FATORIAL: "))
c = n1
print("{}! = " .format(n1), end='')
for n1 in range(1,n1):
    print("{}".format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c = c - 1
print("{}".format(fatorial))