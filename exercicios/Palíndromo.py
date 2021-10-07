print("=" * 25)
print("PALÍNDROMO")
print("=" * 25)


pa = str(input("Digite uma frase: ")).strip().upper()
palavra = pa.split() #separar tudo em um vetor/lista
junto = "".join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inversos de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo")

    #COM FATIAMENTO

'''
inverso = junto[::-1]
'''
