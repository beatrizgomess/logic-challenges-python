from datetime import date
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
atual = date.today().year
idade = atual - ano_nascimento
print("Você nasceu no ano de {}".format(ano_nascimento))
print("Você tem {} anos".format(idade))

if idade <= 9:
    print("ATLETA MIRIM")
elif idade > 9 and idade < 14:
    print("ATLETA INFANTIL")
elif idade > 14 and idade < 19:
    print("ATLETA JÚNIOR")
elif idade > 19 and idade < 25:
    print("ATLETA SÊNIOR")
elif idade > 25:
    print("ATLETA MASTER")