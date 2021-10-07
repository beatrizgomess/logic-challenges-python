from datetime import date
Ano_Nascimento = int(input("Ano de nascimento: "))
Atual = date.today().year
idade = Atual - Ano_Nascimento
print("Quem nasceu em {} tem {} anos em {}".format(Ano_Nascimento, idade, Atual))
if idade == 18:
    print("Você precisa se alistar. CHEGOU A HORA")
    
elif idade < 18:
    saldo = 18 - idade
    ano = Atual + saldo
    print("Não está na hora de  se alistar ainda. Falta {} anos. ".format(saldo))
    print("Você vai se alistar em {}".format(ano))
    ano = Atual + saldo
    
elif idade > 18:
    saldo = idade - 18
    print("Já passou da hora de se alistar. Faz {} anos que seu alistamento está atrasado".format(saldo))
    ano = Atual - saldo
    print("Seu alistamento deveria ter sido em {}".format(ano))