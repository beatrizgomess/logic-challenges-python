from random import randint
print("-=-" * 20)
print("JOGO DA ADVINHAÇÃO - TENTE!!")
print("-=-" * 20)
jogo = randint(0,5)
c = 1
print("Pensei no número!! Sua vez! ".format(jogo))
jogador = int(input("Digite o número do seu palpite: "))
while jogo != jogador:
    if jogador > jogo:
        print("Menos...")
    else:
        print("Mais...")
    jogador = int(input("Novamente, digite um número: "))
    c += 1

if jogo == jogador:
    print("Você acertou!!")
    print("Eu pensei exatamente no número {}".format(jogador))
else:
    print("GANHEI!!")
    print("Eu pensei no número: {} e não no {}".format(jogo, jogador))

print("Você acertou na \033[1;44;30m{}º\033[m tentativa".format(c))