print("-=-" * 6)
print("PAR OU IMPAR?")
print("-=-" * 6)
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número {} é um número par".format(numero))
else:
    print("O número {} é um número ímpar".format(numero))