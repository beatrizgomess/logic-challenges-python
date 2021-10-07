nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Segunda Nota: "))

media = (nota1 + nota2) / 2

print("Sua média é \033[;30;47m{:.1f}\033[m".format(media))
if media >= 7:
    print("Você está \033[;30;44mAPROVADO\033[m")
elif media >= 5 and media <= 6.9:
    print("Você está em \033[;30;43mRECUPERAÇÃO\033[m")
elif media < 5.0:
    print("Você está \033[;30;41mREPROVADO\033[m")