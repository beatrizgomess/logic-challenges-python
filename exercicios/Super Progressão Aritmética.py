print("=" * 40)
print("SUPER PROGRESSÃO ARITMÉTICA")
print("=" * 40)


i = total = 0
nv = 1

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo = termo1 + (10 - 1) * razao


while i <= 9:
        termos = termo1 + i * razao
        i = i + 1
        total = total + i
        print("{}".format(termos), end='>> ')
while nv != 0:
    nv = int(input("\nDeseja mais quantos termos: Se quiser finalizar: "))
    total = i + nv - 1
    while i <= total:
        termos = i * razao
        i = i + 1
        print("{}".format(termos), end=">> ")
print("TEMOS {} TERMOS".format(total))

