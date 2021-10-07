print("{:=^40}".format(" Sistema de Caixa Eletrônico "))


print("{:=^40}".format("CÉDULAS DISPONÍVEIS"))
print("[1] - R$50")
print("[2] - R$20")
print("[3] - R$10")
print("[4] - R$1")

saque = int(input("Quanto você quer sacar? R$"))

notas = 50
ced20 = 20
ced10 = 10
ced1 = 1    
retirar = cont = 0

while True:    
    
    if saque >= notas:
        retirar = saque - notas
        cont = cont + 1
        print(saque, cont, notas)
        
        if retirar < notas:
                    notas = 20
                    retirar = saque - notas
                    cont = cont + 1
                    print(retirar, cont, notas)
        elif retirar < notas:
                    notas = 10
                    retirar = saque - notas
                    cont = cont + 1  
                    print(retirar, cont, notas) 
        elif retirar < notas:
                    notas = 1
                    retirar = saque - notas
                    cont = cont + 1
                    print(retirar, cont, notas)
        
        if retirar == 0:
                break
        

    
 

            

        
    
    

        

    


    
   





      

