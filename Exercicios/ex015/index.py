import random 
alunos = ["Pabro", "CHICA", "cunha", "Mário"]
sorteado = random.choice(alunos)
print("O aluno sorteado foi {}".format(sorteado))


primerio = input("Digite o nome do primerio aluno: ")
segundo = input("Digite o nome do segundo aluno: ")
terceiro = input("Digite o nome do terceiro aluno: ")
quarto = input("Digite o nome do quarto aluno: ")

escolhido = [primerio, segundo, terceiro, quarto]

escolhido = random.choice(escolhido)

print("O aluo sorteado foi {}".format(escolhido))
