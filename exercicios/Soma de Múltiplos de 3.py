
print("=" * 20)
print("SOMA DE MÚLTIPLOS DE TRÊS")
print("=" * 20)

soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        soma = n + soma
print("\n A soma de todos os valores {} é = {}".format(cont, soma))
print("FIM DO PROGRAMA")