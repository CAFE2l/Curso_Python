from time import sleep
import random
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

numero = random.randint(0, 10)
fim = "Fim de Jogo!"

print(f"{estilos['negrito']}{cores['vermelho']}{"==" * 10}{"======Pensador======"}{"==" * 10}{estilos['reset']}")
print(f"{estilos['negrito']}{fundo['roxo']}{cores['amarelo']}Vou pensar em um número entre 0 e 10. Tente adivinhar...   {estilos['reset']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"===" * 20}{estilos['reset']}")

tentativa = -1  # valor inicial só para entrar no loop

while tentativa != numero:
    tentativa = int(input(f"Chute um número de {estilos['negrito']}{cores['azul']}0 a 10: {cores['limpa']}"))
    print("PROCESSANDO...")
    sleep(1)

    if tentativa == numero:
        print(f"{estilos['negrito']}{cores['verde']}Parabéns! Você acertou!{cores["limpa"]}")
    else:
        print(f"{cores['vermelho']}{estilos['negrito']}Errou! {cores['limpa']}Tente novamente...")

print(f"O número necessário de tentativas para me vencer foi de:{cores['amarelo']}{estilos['negrito']} {tentativa} tentativas.{cores['limpa']}")
print(f"{estilos['negrito']}{cores['pretoebranco']}{fim.center(55)}{cores['limpa']}")

#Solução do Guana
computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos..")
print("Acertou! com {} tentativas. Parabéns!".format(palpites))
