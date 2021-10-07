print("=" * 40)
print("TABUADA V3.0")
print("=" * 40)

#? UTILIZANDO WHILE
n = 0
c = cont = resp = 1
while True:
    n = int(input("Digite um número para saber sua tabuada: "))
    print("Para sair digite -1")
    print("=" * 40)
    #cont += 1
    #? n < 0: - qualquer número negativo
    if n == -1:
        break
    for c in range(1,11):
        resp = n * c
        print(f"\t\t{n} X {c} = {resp}")
    print("=" * 40)
print("OBRIGADA POR UTILIZAR O PROGRAMA")
#print(f"Você visualizou a tabuada de {cont} números")
    
#? UTILIZANDO FOR 
n = 0
tb = na = 1
n = int(input("Digite um valor: "))
for na in range(1, 10):
    tb = n * na
    print(tb)