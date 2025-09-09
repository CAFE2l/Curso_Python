
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
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m"
}

import random
from time import sleep

print("🎲" * 20)
print(f"    {cores['amarelo']}{estilos['negrito']}{estilos['italico']}JOGO DE DADOS - 4 JOGADORES{estilos['reset']}")
print("🎲" * 20)

# Dicionário para armazenar os resultados
jogadores = {}

# Lista com nomes dos 4 jogadores
nomes = ["Jogador1", "Jogador2", "Jogador3", "Jogador4"]

# Cada jogador joga o dado
print(f"\n{estilos['negrito']}{cores['amarelo']}--- {cores['cinza']}JOGANDO OS DADOS {cores['amarelo']}---{estilos['reset']}")
for nome in nomes:
    print(f"{cores['vermelho']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}{nome}{cores['cinza']} está jogando o dado...{estilos['reset']}")
    sleep(1)  # Pausa dramática
    
    resultado = random.randint(1, 6)  # Sorteia número de 1 a 6
    jogadores[nome] = resultado       # Salva no dicionário
    
    print(f"{cores['verde']}{estilos['negrito']}{nome} {cores['cinza']}tirou: {cores['vermelho']}{resultado}{cores['limpa']}")

print(f"\n{estilos['negrito']}{cores['roxo']}--- {cores['vermelho']}RESULTADOS INICIAIS {cores['roxo']}---{estilos['reset']}")
for nome, resultado in jogadores.items():
    print(f"{cores['verde']}{estilos['negrito']}{nome}{cores['cinza']}: {cores['vermelho']}{resultado}{cores['limpa']}")

# ORDENAÇÃO: do maior para o menor (vencedor primeiro)
print(f"\n{estilos['negrito']}{cores['roxo']}--- {cores['amarelo']}CLASSIFICAÇÃO FINAL {cores['roxo']}---")
print(f"{cores['vermelho']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}(Do maior para o menor){estilos['reset']}")

# Método 1: usando sorted() com lambda
jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

posicao = 1
for nome, resultado in jogadores_ordenados:
    if posicao == 1:
        print(f"🏆 {estilos['negrito']}{cores['verde']}{posicao}º {cores['cinza']}lugar: {nome} - {cores['amarelo']}{resultado} {cores['cinza']}pontos {cores['verde']}(VENCEDOR!){estilos['reset']}")
    elif posicao == 2:
        print(f"🥈 {estilos['negrito']}{cores['amarelo']}{posicao}º {cores['cinza']}lugar: {nome} - {cores['amarelo']}{resultado} {cores['cinza']}pontos{cores['limpa']}")
    elif posicao == 3:
        print(f"🥉 {estilos['negrito']}{cores['vermelho']}{posicao}º {cores['cinza']}lugar: {nome} - {cores['amarelo']}{resultado} {cores['cinza']}pontos{cores['limpa']}")
    else:
        print(f"   {estilos['negrito']}{cores['cinza']}{posicao}º {cores['cinza']}lugar: {nome} - {cores['amarelo']}{resultado} {cores['cinza']}pontos{cores['limpa']}")
    posicao += 1

print(f"{cores['azul']}{estilos['negrito']}{"\n" + "="*20}{estilos['reset']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}JOGO FINALIZADO!{estilos['reset']}")
print(f"{cores['azul']}{estilos['negrito']}{"="*20}{estilos['reset']}")