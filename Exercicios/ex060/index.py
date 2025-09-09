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
print(f"{estilos['negrito']}{cores['azul']}{"==" * 5 }{cores['vermelho']}RAZÃO{cores['azul']}{"==" * 5}{cores['limpa']}")
menu = "Razão de uma PA"
print(f"{estilos['negrito']}{estilos['italico']}{fundo['roxo']}{cores['amarelo']}{menu.center(25)}{cores['limpa']}")
print(f"{cores['azul']}{estilos['negrito']}{"==="*8 + "="}{cores['limpa']}")
# Lê o primeiro termo e a razão da PA

primeiro = int(input(f"{estilos['negrito']}{estilos['italico']}Primeiro termo: {estilos['reset']}"))
razao = int(input(f"{estilos['negrito']}{estilos['italico']}Razão: {estilos['reset']}"))

# Inicializa variáveis de controle
termo = primeiro   # termo atual da PA
cont = 0           # quantos termos já mostramos

# Loop: mostra exatamente 10 termos
while cont < 10:
    # imprime o termo e coloca ' -> ' até o penúltimo;
    # no último termo, quebra a linha
    print(f"{cores['pretoebranco']}{estilos['italico']}{termo}{cores['limpa']}", end=f"{cores['azul']}{estilos['negrito']} -> {cores['limpa']}" if cont < 9 else "\n")

    termo += razao   # próximo termo da PA
    cont += 1        # incrementa o contador


print(f"{cores['amarelo']}{estilos['negrito']}⭐Acabou🎉")
