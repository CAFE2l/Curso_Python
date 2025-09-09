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
    "branco": "\033[40m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m",
    'vermelho_claro': '\033[101m',
    'verde_claro': '\033[102m',
    'amarelo_claro': '\033[103m',
    'azul_claro': '\033[104m',
    'roxo_claro': '\033[105m',
    'ciano_claro': '\033[106m',
    'cinza_claro': '\033[107m'
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
    "duplosublinhado": "\033[21m",  # Sublinhado duplo
    "normal": "\033[22m",           # Desativa negrito e fraco
    "semitalico": "\033[23m",       # Desativa itálico
    "sem_sublinhado": "\033[24m",   # Desativa sublinhado
    "sem_inverso": "\033[27m",      # Desativa inverso
    "visivel": "\033[28m",          # Desativa invisível
    "sem_tachado": "\033[29m"       # Desativa tachado
}
from random import randint


pim = "IMPAR OU PAR"
print(f"{estilos['negrito']}{cores['amarelo']}{"==="*5}{cores['vermelho']}{"PARIDADE"}{cores['amarelo']}{"==="*5+"="}{estilos['reset']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{estilos['italico']}{pim.center(39)}{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"==="*13}{estilos['reset']}")

vitórias = 0  # contador de vitórias consecutivas

ola = input(f"{estilos['negrito']}{cores['azul']}Quer jogar par ou ímpar? {cores['roxo']}[S/N]:{estilos['reset']} ").upper()
if ola == "S":
    print(f"{estilos['sublinhado']}{estilos['negrito']}{cores['azul']}Você escolheu jogar par ou ímpar!{estilos['reset']}")
    while True:
        jogador = input(f"{cores['roxo']}{estilos['negrito']}PAR{estilos['reset']} ou {estilos['negrito']}{cores['roxo']}ÍMPAR? {estilos['reset']}").upper()
        if jogador not in ["PAR", "IMPAR"]:
            print(f"{estilos['negrito']}{cores['vermelho']}Opção inválida! Tente novamente.{estilos['reset']}")
            continue

        numero = int(input(f"{estilos['negrito']}{cores['ciano']}Digite um número de {cores['roxo']}1{estilos['reset']} a {cores["roxo"]}{estilos['negrito']}10:{estilos['reset']} "))
        computador = randint(1, 10)
        print(f"{estilos['negrito']}Você jogou {cores['vermelho']}{numero}{estilos['reset']}{estilos['negrito']} e o computador jogou {cores['vermelho']}{computador}.{estilos['reset']}")

        soma = numero + computador
        if (soma % 2 == 0 and jogador == "PAR") or (soma % 2 == 1 and jogador == "IMPAR"):
            print(f"{cores['verde']}{estilos['negrito']}{estilos['italico']}Você ganhou!{estilos['reset']}")
            vitórias += 1
        else:
            print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}Você perdeu!{estilos['reset']}")
            break  # sai do loop quando perder

    print(f"{cores['amarelo']}{estilos['negrito']}Fim de jogo!{estilos['reset']} Você teve {estilos['negrito']}{cores['vermelho']}{vitórias} {cores['verde']}vitórias consecutivas{estilos['reset']}")
else:
    print(f"{cores['cinza']}{estilos['italico']}Você escolheu não jogar.{estilos['reset']}")
