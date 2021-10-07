print("=" * 40)
print("ESTATÍSTICA DO PRODUTO")
print("=" * 40)

continuar = "S"
maisbarato = " "
total = custa1000 = menor = cont = 0

while True:
    while continuar in "S":
        nome = str(input("Nome do produto: "))
        preco = float(input("Preço: R$"))
        cont = cont + 1
        continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
        while continuar not in "SN":
            continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
            
        total = total + preco
        
        if cont == 1 or preco < menor:
            menor = preco
            maisbarato = nome
        
        if preco >= 1000:
            custa1000 = custa1000 + 1

        
    if continuar == "N":
        print("{:-^40}".format("FIM DO PROGRAMA"))
        break
        
print("=" * 40)
print("\t\tRESULTADOS")
print("=" * 40)
print(f"TOTAL DA COMPRA = R${total:.2f}")
print(f"PRODUTOS ACIMA DE R$1000 = {custa1000}")
print(f"PRODUTO MAIS BARATO: {maisbarato} de R${menor}") 