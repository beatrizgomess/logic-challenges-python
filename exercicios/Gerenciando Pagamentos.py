print("=" * 30)
print("GERENCIADOR DE PAGAMENTOS")
print("=" * 30)

compra = float(input("Digite o valor da compra: "))

print("[ 1 ] - A VISTA - DINHEIRO/CHEQUE")
print("[ 2 ] - DÉBITO")
print("[ 3 ] - 2x NO CARTÃO")
print("[ 4 ] - 3X OU MAIS NO CARTÃO")

op = int(input("DIGITE UMA DAS OPÇÕES ACIMA: "))

if op == 1:
    desconto = compra * 0.10
    valor_final = compra - desconto
    print("Sua compra de \033[1;30;46mR${}\033[m fica \033[1;30;46mR${}\033[m por conta de um desconto de \033[1;30;46mR${}\033[m".format(compra, valor_final, desconto))

elif op == 2:
    desconto = compra * (5/100)
    valor_final = compra - desconto
    print("Sua compra de \033[1;30;46mR${}\033[m fica no valor de \033[1;30;46mR${}\033[m por conta de um desconto de \033[1;30;46mR%{:.2f}\033[m ".format(compra, valor_final, desconto))

elif op == 3:
    valor_final = compra/2
    print("Sua compra de \033[1;30;46mR${} será parcelada em 2x, de \033[1;30;46mR${}\033[m SEM JUROS".format(compra, valor_final))

elif op == 4:
    parcelas = int(input("DIGITE A QUANTIDADE DE PARCELAS: "))
    print("CALCULANDO...")
    acrescimo = compra * (20/100)
    parcelados = (compra + acrescimo)/parcelas
    valor_final = compra + acrescimo
    print("Sua compra será parcelada em \033[1;30;46{}x\033[m".format(parcelas))
    print("As parcelas ficam cada uma no valor de \033[1;30;46mR${}\033[m COM JUROS de \033[1;30;46mR${}\033[m".format(parcelados, acrescimo))
    print("O TOTAL de sua compra foi para \033[1;30;46mR${:.2f}\033[m".format(valor_final))

else:
    print("=" * 50)
    print("OPÇÃO INVÁLIDA. POR FAVOR INSIRA UMA OPÇÃO VALIDA")
    print("=" * 50)