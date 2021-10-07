import random

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(alunos)
print("Parabéns " + sorteio + ". Você foi escolhida(o) para apagar o quadro")