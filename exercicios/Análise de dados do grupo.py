print("=" * 40)
print("\tAnalisando Dados")
print("=" * 40)

n = 1
contPessoas = contHomens = contMulheres = 0
continuar = "S"
print("POR FAVOR INFORME OS DADOS ABAIXO: ")
print("=" * 40)
while True: 
    while continuar in "S":
        print(f"{n} - PESSOA")
        n = n + 1
        sexo = str(input("Sexo: [F][M] ")).upper().strip()[0]
        while sexo not in "FM":
            sexo = str(input("Sexo inválido!! FEMININO OU MASCULINO: ")).upper()[0]
        idade = int(input("Idade: "))
        continuar = str(input("Deseja Continuar? [S/N]: ")).upper()
        
        print("=" * 40)        
        if idade > 18:
            contPessoas =  contPessoas + 1
                
        if sexo == "M":
            contHomens = contHomens + 1
                
        if idade < 20 and sexo == "F":
            contMulheres = contMulheres + 1
                
    else:
        print("\tPrograma Finalizado!")
        break
    
print("=" * 40)
print("\tRESULTADOS DA ANÁLISE")
print("=" * 40)
print(f"{contPessoas} PESSOA(S) tem mais de 18 ano(s)")
print(f"{contHomens} HOMEM(S) foram cadastrado(s)")
print(f"{contMulheres} MULHERE(S) tem menos de 20 ano(s)")