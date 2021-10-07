print("=" * 40)
print("PROGRESSÃO ARITMÉTICA")
print("=" * 40)


i = 0

termo1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo = termo1 + (10 - 1) * razao


while i <= 10:
        termos = termo1 + i * razao
        i = i + 1
        print("{}".format(termos), end='>> ')