frase = str(input("Digite uma frase: ")).strip().upper()
# pode adequar a contagem natural do usuario adicionando +1 ao count e find
print("A frase possui {} letra ""A"" ".format(frase.count("A")))
print("Apareceu a primeira vez na posição: {}".format(frase.find("A")))
ult = frase.__len__() - 1
print("Apareceu a última vez na posição:  {}".format(ult))
print(".".join(frase))