print("*" * 22)
print("\tSOMA DOS PARES")
print("*" * 22)

print("DIGITE 6 NÚMEROS")

soma = 0
cont = 0
for n in range(1,7):
    n = int(input("Digite o {}º número: ".format(n)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print("Você digitou {} números pares".format(cont))
print(f"A soma dos pares é {soma}")
print("FIM DO PROGRAMA")