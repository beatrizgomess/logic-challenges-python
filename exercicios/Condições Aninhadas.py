# If - elif - else
# Elif - testar várias condições e quando apenas uma tem que passar
# Elif = Else If

nome = str(input("Digite seu nome: "))
if nome == "Beatriz":
    print("Você é a futura esposa de Maria Eduarda")
elif nome == "Eduarda":
    print("Seu nome é Maria Eduarda e vai casar com Lilian Beatriz")
elif nome in "Ana Claudia Jéssica Juliana":
    print("Seu nome é feminino")
else:
    print("Você não é nada para Eduarda {}, não como Beatriz é para ela".format(nome))

