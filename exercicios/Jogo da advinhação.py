from random import randint
print("-=-" * 20)
print("JOGO DA ADVINHAÇÃO - TENTE!!")
print("-=-" * 20)
jogo = randint(0,5)
print("Pensei no número!! Sua vez! ".format(jogo))
jogador = int(input("Digite o número: "))
if jogo == jogador:
    print("Você acertou!!")
    print("Eu pensei exatamente no número {}".format(jogador))
else:
    print("GANHEI!!")
    print("Eu pensei no número: {} e não no {}".format(jogo, jogador))
