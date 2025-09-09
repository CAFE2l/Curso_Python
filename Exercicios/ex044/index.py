import random
from time import sleep
from random import randint
# Dicionários de cores, fundos e estilos
cores = {
    "limpa": "\033[m",
    'vermelho': "\033[31m",
    'verde': "\033[32m",
    'amarelo': "\033[33m",
    'azul': "\033[34m",
    'roxo': "\033[35m",
    'ciano': "\033[36m",
    'cinza': "\033[37m",
    'pretoebranco': '\033[7;30m'
}

fundo = {
    "branco": "\033[m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m"
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m"
}

# Lista de opções
objects = ["pedra", "papel", "tesoura"]

# Escolha do computador
escolha_pc = random.choice(objects)

print("-=-" * 5)
print("JOKENPÔ")
print("-=-" * 5)

print("1) pedra")
print("2) papel")
print("3) tesoura")

item = int(input("Escolha uma opção: "))

# Converter o número do jogador para a jogada correspondente
if item in [1, 2, 3]:
    escolha_jogador = objects[item - 1]
else:
    print("Opção inválida")
    exit()

# Mostrar escolhas
print(f"\nVocê escolheu {cores['verde']}{estilos['negrito']}{escolha_jogador}{cores['limpa']}")
print(f"O computador escolheu {cores['vermelho']}{estilos['negrito']}{escolha_pc}{cores['limpa']}")

# Determinar resultado
if escolha_jogador == escolha_pc:
    print(cores['amarelo']+  estilos['negrito'] + "Empate!" + cores['limpa'])
elif (
    (escolha_jogador == "pedra" and escolha_pc == "tesoura") or
    (escolha_jogador == "papel" and escolha_pc == "pedra") or
    (escolha_jogador == "tesoura" and escolha_pc == "papel")
):
    print(cores['verde'] + estilos['negrito']+ "Você ganhou!" + cores['limpa'])
else:
    print(cores['vermelho'] + estilos['negrito']+ "Você perdeu!" + cores['limpa'])


#Solução do Guaná:
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print()
print("KEN")
sleep(1)
print()
print("PO!!!")
sleep(1)

print("-="*11)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("-="*11)
if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:  
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE") 
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("""EMPATE""")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!")