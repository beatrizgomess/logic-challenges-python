from random import randint
from time import sleep
print("=" * 25)
print("\t\tJO KEN PO")
print("=" * 25)
print("[ 0 ] - PEDRA")
print("[ 1 ] - PAPEL")
print("[ 2 ] - TESOURA")

print("-=-" * 25)
jogador1 = int(input("Qual sua jogada?"))
print("-=-" * 25)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!\n")
sleep(1)

jogador2 = randint(0,2)

if jogador1 == 0:
    print("JOGADOR 1 JOGOU PEDRA")
elif jogador1 == 1:
    print("JOGADOR 1 JOGOU PAPEL")
elif jogador1 == 2:
    print("JOGADOR 1 JOGOU TESOURA")
else:
    print("OPÇÃO INVÁLIDA")

if jogador2 == 0:
    print("JOGADOR 2 JOGOU PEDRA")
elif jogador2 == 1:
    print("JOGADOR 2 JOGOU PAPEL")
elif jogador2 == 2:
    print("JOGADOR 2 JOGOU TESOURA")
else:
    print("OPÇÃO INVÁLIDA")

if jogador1 == 0:
    if jogador2 == 0:
        print("EMPATE")
    elif jogador2 == 1:
        print("JOGADOR 2 VENCE")
    elif jogador2 == 2:
        print("JOGADOR 1 VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif jogador1 == 1:
    if jogador2 == 0:
        print("JOGADOR 1 VENCE")
    elif jogador2 == 1:
        print("EMPATE")
    elif jogador2 == 2:
        print("JOGADOR 2 VENCE")
    else:
        print("JOGADA INVÁLIDA")

elif jogador1 == 2:
    if jogador2 == 0:
        print("JOGADOR 2 VENCE")
    elif jogador2 == 1:
        print("JOGADOR 1 VENCE")
    elif jogador2 == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")