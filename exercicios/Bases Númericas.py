print("=" * 40)
print("PROGRAMA DE CONVERSÃO DE BASES NÚMERICAS ")
print("=" * 40)
n = (int(input("Digite um número inteiro (ESTE NÚMERO ESTÁ NA BASE DECIMAL):  ")))

print("=" * 60)
print("OPÇÕES")
print("[ 1 ]- BINÁRIO")
print("[ 2 ]- OCTAL")
print("[ 3 ] - HEXADECIMAL")
op = int(input("ESCOLHA SUA OPÇÃO: "))
print("=" * 60)

if op == 1:
    print("BINÁRIO")
    print("Resultado: O número \033[1;30;45m{}\033[m em BINÁRIO é \033[1;30;45m{}\033[m".format(n, bin(n)[2:]))
elif op == 2:
    print("OCTAL")
    print("Resultado: O número {} é em OCTAL {}".format(n, oct(n)[2:]))

elif op == 3:
    print("HEXADECIMAL")
    print("Resultado: O número {} é em HEXADECIMAL {}".format(n, hex(n)[2:]))
else:
    print("OPÇÃO INVÁLIDA!!")

