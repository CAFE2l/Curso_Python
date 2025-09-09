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

frase = "Listas dos Números Pares e Ímpares"

print(f"{estilos['negrito']}{cores['roxo']}{'==='*5}{cores['cinza']}PARES-E-ÍMPARES{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['vermelho']}{'==='*5+"="}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{'==='*15+'='}{estilos['reset']}")


pares = [];
numeros = []
impares = []
for _ in range(0, 7):
    num = int(input(f"{cores['cinza']}{estilos['negrito']}Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        print(f"{cores['azul']}{estilos['negrito']}O número {cores['verde']}{num} {cores['cinza']}é {cores['verde']}par{estilos['reset']}.")
        pares.append(num)
    elif num % 2 == 1:
        print(f"{cores['azul']}{estilos['negrito']}O número {cores['vermelho']}{num} {cores['cinza']}é {cores['vermelho']}ímpar{estilos['reset']}.")
        impares.append(num)
print(f"{cores['amarelo']}{estilos['negrito']}{'==='*15+'='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}Números {cores['amarelo']}pares{cores['cinza']} digitados: {cores['verde']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}{sorted(pares)}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}Números {cores['amarelo']}ímpares{cores['cinza']} digitados: {cores['vermelho']}{estilos['italico']}{estilos['sublinhado']}{sorted(impares)}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}Todos os números digitados: {cores['azul']}{estilos['sublinhado']}{estilos['italico']}{sorted(numeros)}{estilos['reset']}")