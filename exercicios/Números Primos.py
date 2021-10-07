print("=" * 25)
print("\tNÚMEROS PRIMOS")
print("=" * 25)

num = int(input("Digite um número: "))
tot = 0
resp = int
for contador in range(1, num + 1):
    if num % contador == 0:
        print('\033[34m', end="")
        tot += 1
    else:
        print("\033[31m", end = "")
    print("{} ".format(contador), end=" ")
print ("\n\033[mO numero {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("Por isso ELE É PRIMO")
else:
    print("Por isso ELE NÃO É PRIMO")


