print("1 - DOLÁR")
print("2 - EURO")
print("3 - REAL")
moeda = float(input(("Qual a sua moeda? ")))

if moeda == 1:
    print("DOLÁR\n")
    casa = float(input("Qual o valor da casa? U$: "))
    salario = float(input("Qual o valor do seu salário? U$"))
    parcelas = int(input("Em quantos anos você vai pagar? "))
    parcelas = parcelas * 12
    prestação = casa / parcelas
    maxima = salario * (30 / 100)
    print("Da um total de {} parcelas".format(parcelas))
elif moeda == 2:
    print("EURO\n")
    casa = float(input("Qual o valor da casa? "))
    salario = float(input("Qual o valor do seu salário? "))
    parcelas = int(input("Em quantos anos você vai pagar? "))
    maxima = salario * (30 / 100)
    print("Da um total de {} parcelas".format(parcelas))

elif moeda == 3:
    print("REAL\n")
    casa = float(input("Qual o valor da casa? "))
    salario = float(input("Qual o valor do seu salário? "))
    parcelas = int(input("Em quantos anos você vai pagar? "))
    maxima = salario * (30 / 100)
    print("Da um total de R${} parcelas".format(parcelas))


if prestação < (30/100) * salario:
    print("Parabéns!! EMPRESTIMO CONSEDIDO!! Você pode financiar sua casa")
    print("A sua prestação fica no valor de \033[1;37;40m {:.2f}\033[m ao mês".format(prestação))
elif prestação == (30/100) * salario:
    print("Parabéns!! EMPRETIMO CONSEDIDO! Você pode financiar sua casa")
    print("A sua prestação fica no valor de \033[1;37;40m {:.2f}\033[m ao mês".format(prestação))
elif prestação > (30/100) * salario:
    print("Desculpe, EMPRESTIMO NEGADO!! O valor da prestação compromete seu salário. \nNão é seguro financinar uma casa agora")
    print("A sua prestação ficaria no valor de \033[1;37;40m {:.2f}\033[m ao mês".format(prestação))

print("A parcela máxima que você pode pagar é até \033[1;30;45m{:.2f}\033[m e sua parcela está no valor de \033[1;30;45m{:.2f}\033[m".format(maxima, prestação))