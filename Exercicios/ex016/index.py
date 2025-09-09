import random

ordem = ["Pabro", "CHICA", "cunha", "Mário"]
sorteio = random.shuffle(ordem)
print(ordem)


primerio = input("Digite o nome do primerio aluno: ")
segundo = input("Digite o nome do segundo aluno: ")
terceiro = input("Digite o nome do terceiro aluno: ")
quarto = input("Digite o nome do quarto aluno: ")

alunos = [primerio,segundo,terceiro,quarto]
escolhido = random.shuffle(alunos)
print("A ordem de apresentação será: {}".format(alunos))