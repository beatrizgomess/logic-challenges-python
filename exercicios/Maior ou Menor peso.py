maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da Pessoa: ".format(p)))
    if p == 1:
        maior = peso #80
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso é \033[36m{}kg\033[m".format(maior))
print("O menor peso é \033[36m{}kg\033[m".format(menor))
