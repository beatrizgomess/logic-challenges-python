nomeC = str(input("Digite seu nome completo: "))
print(nomeC.title().strip())

print("NOME COMPLETO MAIUSCULO: ")
print(nomeC.upper())

print("NOME COMPLETO MINUSCULO: ")
print(nomeC.lower())

print("TAMANHO DO NOME: ")
print(len(nomeC))

# Sem Espaços
m = len(nomeC) - nomeC.count(" ")
print(m)

# Guanabara fez assim:
print("Tamanho do nome: {}".format(len(nomeC) - nomeC.count(" ")))


div = nomeC.split()
print("TAMANHO DO PRIMEIRO NOME: {}".format(len(div[0])))
# Guanabara fez assim:
print("Tamanho do primeiro nome: {} ".format(nomeC.find(" ")))
