from time import sleep
print("=" * 35)
print("\t\tCALCULADORA")
print("=" * 35)

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
escolha = 0
maior = 0
while escolha != 5:
    print("MENU")
    print("1 - SOMA")
    print("2 - MULTIPLICAR")
    print("3 - MAIOR")
    print("4 - NOVOS NÚMEROS")
    print("5 - SAIR DO PROGRAMA")
    escolha = int(input("Opção: "))
    if escolha == 1:
        print("SOMA")
        soma = n1 + n2
        print("\033[43m {} + {} = {}\033[m".format(n1, n2, soma))
    elif escolha == 2:
        print("\033[42m MULTIPLICAÇÃO \033[m")
        mult = n1 * n2
        print("\033[42m {} X {} = {}\033[m".format(n1, n2, mult))

    elif escolha == 3:
        print("\033[45mMAIOR NUMERO \033[m")
        if n1 > n2:
            maior = n1
            print("\033[45mMaior: {}\033[m".format(maior))
        else:
            maior = n2
            print("\033[45mMaior: {}\033[m".format(maior))

    elif escolha == 4:
        print("\033[44m NOVOS NÚMEROS \033[m")
        n1 = int(input("Novo numero: "))
        n2 = int(input("Outro numero: "))
    elif escolha == 5:
        print("\033[41m SAIR DO PROGRAMA \033[m")

    else:
        print("\033[41m OPÇÃO INVÁLIDA \033[m")
    print("=" * 35)
    sleep(2)
print("FIM")
