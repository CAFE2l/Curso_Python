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

frase = "MATRIZ 3X3"

print(f"{estilos['negrito']}{cores['azul']}{'=='*5}{cores['cinza']}MATRIZ_V2.0({cores['azul']}3{cores['cinza']}X{cores['vermelho']}3{cores['cinza']}){cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['vermelho']}{'=='*6 +'='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{'==='*13}{estilos['reset']}")

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"{cores['cinza']}{estilos['negrito']}Digite um valor para {cores['azul']}{estilos['italico']}{estilos['sublinhado']}[{linha}, {coluna}]:{cores['limpa']}"))

print(f"{cores['azul']}{estilos['negrito']}{"-=" * 30}{cores['limpa']}")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{estilos['negrito']}{cores['verde']}[{matriz[l][c]:^5}]", end="")
    print()
if (linha % 2 == 0) and (coluna % 2 == 0):
    print(f"{cores['amarelo']}{estilos['negrito']}Os valores pares digitados foram: ", end="")
    for l in range(0, 3):
        for c in range(0, 3):
            if matriz[l][c] % 2 == 0:
                print(f"{matriz[l][c]}", end=" ")
    print()
print(f"{cores['cinza']}a soma dos {cores['verde']}pares {cores['cinza']}é: {cores['verde']}{estilos['negrito']}{sum([matriz[l][c] for l in range(0, 3) for c in range(0, 3) if matriz[l][c] % 2 == 0])}{cores['limpa']}")
print(f"{cores['cinza']}{estilos['negrito']}a soma dos valores da {cores['vermelho']}terceira coluna {cores['cinza']}é: {cores['vermelho']}{estilos['negrito']}{sum([matriz[l][2] for l in range(0, 3)])}{cores['limpa']}")
print(f"{cores['cinza']}{estilos['negrito']}o maior valor da {cores['roxo']}segunda linha {cores['cinza']}é: {cores['roxo']}{estilos['negrito']}{max([matriz[1][c] for c in range(0, 3)])}{cores['limpa']}")
print(f"{cores['azul']}{'-=' * 30}{cores['limpa']}")