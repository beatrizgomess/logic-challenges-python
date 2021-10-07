print("=" * 20)
print("COMPARANDO NÚMEROS")
print("=" * 20)
n1 = int(input("1º número: "))
n2 = int(input("2º número: "))

print("=" * 33)
print("RESULTADO: MAIOR E MENOR NÚMERO ")
print("=" * 33)
if n1 > n2:
    print("O PRIMEIRO valor, \033[1;44;30m{}\033[m, é maior que o SEGUNDO valor \033[1;44;30m{}\033[m".format(n1, n2))
    #print("O O SEGUNDO valor,  \033[1;30;45m{}\033[m, é menor que o PRIMEIRO valor \033[1;30;45m{}\033[m".format(n2, n1))
elif n2 > n1:
    print("O SEGUNDO valor, \033[1;45;30m{}\033[m, é maior que o PRIMEIRO valor \033[1;45;30m{}\033[m".format(n2, n1))
    #print("O PRIMEIRO valor, \033[1;30;45m{}\033[m é menor que o SEGUNDO valor \033[1;30;45m{}\033[m".format(n1, n2))
else:
    print("NÃO EXISTE VALOR MAIOR OU MENOR, OS DOIS SÃO IGUIS")
