print("=========================")
print("ÍNDICE DE MASSA CORPOREA")
print("=========================\n")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)
print("Seu IMC é {:.2f}".format(imc))
if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc >= 18.5 and imc <= 25.0:
    print("PESO IDEAL")
elif imc > 25.0 and imc < 30.0:
    print("SOBREPESO")
elif imc > 30 and imc < 40:
    print("OBESIDADE")
elif imc > 40:
    print("OBESIDADE MÓRBIDA")