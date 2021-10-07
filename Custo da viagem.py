distancia_viagem = float(input("Qual a distância da viagem? Em KM"))
if distancia_viagem <= 200:
    passagem = distancia_viagem * 0.50
    print("Sua viagem de {:.1f}Km custa R${:.2f}".format(distancia_viagem, passagem))
else:
    if distancia_viagem >= 200:
        passagem = distancia_viagem * 0.45
        print("Sua viagem de {:.1f}Km custa R${:.2f}".format(distancia_viagem, passagem))