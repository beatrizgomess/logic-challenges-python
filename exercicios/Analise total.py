print("=" * 50)
print("\tANÁLISE TOTAL COM BASE EM UMA POPULAÇÃO")

maior = 0
menor = 0
Cont_M = 0
Cont_H = 0
M_menor20 = 0
media = 0
idadehomemvelho = 0

for pessoas in range(1, 5):
    print("========================= {}º PESSOA =========================".format(pessoas))
    nome = str(input("Digite seu nome: ")).title()
    idade = int(input("Digite sua idade: ".format(pessoas)))
    sexo = str(input("Digite o sexo: ")).upper()
# =====================================================
        # IDADES
    if pessoas == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
# =======================================================
        # CONTADOR
    if sexo == "F":
        Cont_M += 1
    else:
        if sexo == "M":
            Cont_H += 1
# ============================================
    # QUANTAS MULHERES MENORES DE 20

    if sexo == "F" and idade < 20:
        M_menor20 += 1
# ============================================
    # HOMEM MAIS VELHO

    if sexo == "M":
        if idade > idadehomemvelho:
            idadehomemvelho = idade
            homem_velho = nome
# ==============================================
    # MÉDIA DAS IDADES
    media += idade / 4
# ==============================================

print("=" * 50)
print("\t\t\tRESPOSTAS")
print("=" * 50)
print("MAIOR IDADE: {} ANOS".format(maior)) # Pessoa mais velha
print("MENOR IDADE: {} ANOS".format(menor)) # Pessoa mais nova
print("MÉDIA: {:2}".format(media)) # Média das idades
print("QUANTIDADE MULHERES: {}".format(Cont_M)) # Quantas mulheres
print("QUANTIDADE HOMENS: {}".format(Cont_H)) # Quantos Homens
print("MULHERES MENORES DE 20: {}".format(M_menor20)) # Quantas mulheres menores de 20
print("O HOMEM MAIS VELHO: NOME = {} | IDADE = {}".format(homem_velho, idadehomemvelho)) # Homem mais velho
