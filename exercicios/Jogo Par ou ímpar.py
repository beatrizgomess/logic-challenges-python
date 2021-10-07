print("=" * 40)
print("\tJOGO PAR OU IMPAR")
print("=" * 40)

print("\t [1] - PAR")
print("\t [2] - ÍMPAR")
import random

jogador = total = 0
computador = 0
contcomp = 0
contjog = 0

while True: 
    print("=" * 40)
    escolha = int(input("Escolha uma opcao: "))
    jogador = int(input("Digite seu número: "))
    print("-" * 40)
    computador = random.randint(0,10)
    total = computador + jogador
    print(f"{jogador} - Jogador + {computador} - Computador = {total}")
    
    if escolha == 1:
        print("Computador escolheu impar entao")
        print("=" * 40)
        if total % 2 == 0:
            print("Deu Par!!")
            print("-" * 40)
            print("Você Ganhou!!")
            print("-" * 40)
            contjog = contjog + 1 
        else:
            print("Deu Impar")
            print("-" * 40)
            print("GAME OVER!! Você Perdeu!!")
            print("-" * 40)
            contcomp = contcomp + 1
            break
        
    elif escolha == 2:
        print("Computador escolheu par entao")
        print("=" * 40)
        if total % 2 >= 1: 
            print("Deu Impar!! ")
            print("-" * 40)
            print("Você Ganhou!!")
            print("-" * 40)
            contjog = contjog + 1
        else:
            print("Deu Par!!")
            print("-" * 40)
            print("GAME OVER!! Você Perdeu!!")
            print("-" * 40)
            contcomp = contcomp + 1
            break
        
    
    
    '''
    if total % 2 >= 1: 
            print("Deu Impar!! ")
            print(f"{jogador} - Jogador + {computador} - (Computador) = {total}")
            contjog = contjog + 1
    elif total % 2 == 0:
            print("Deu Par!!")
            print(f"{jogador} - Jogador + {computador} - (Computador) = {total}")
            contcomp = contcomp + 1
'''            
print("=" * 40)        
print(f"Computador venceu {contcomp} partidas")
print(f"Jogador venceu {contjog} partidas")

            
            