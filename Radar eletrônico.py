velocidade = float(input("Qual a velocidade? Em km: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7

    print("Você ultrapassou o limite de velocidade. Sua multa é de {}".format(multa))
else:
    print("Você não ultrapassou o limite de velocidade")