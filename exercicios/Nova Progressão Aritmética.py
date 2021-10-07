from time import sleep
print("=" * 40)
print("PROGRESSÃO ARITMÉTICA COM WHILE")
print("=" * 40)
i = 0
termo1 = int(input("Digite o primeiro termo"))
razao = int(input("Digite a razão: "))
decimo = termo1 + (10 - 1) * razao

while i <= 9:
    termos = termo1 + i * razao
    i = i + 1
    sleep(1)
    print("{} ".format(termos), end='>> ')
print(end='FIM')





