from datetime import date
atual = date.today().year
maior = 0
menor = 0
for candidatos in range(1,8):
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    idade = atual - ano_nascimento
    print("\t\t\t\t\tSUA IDADE: \033[33m{}\033[m".format(idade))
    if idade >= 21:
        maior = maior + 1

    elif idade < 21:
        menor = menor + 1

print("{} candidatos \033[34m SÃO MAIORES \033[m de idade".format(maior))
print("{} candidatos \033[36m SÃO MENORES \033[m de idade".format(menor))