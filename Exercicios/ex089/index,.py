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

frase = "PROGRAMINHA DE MÉDIA"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5}{cores['cinza']}MÉDIA{cores['vermelho']}{'==='*6 +'='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{'==='*13}{estilos['reset']}")

nome = str(input(f"{cores['azul']}{estilos['negrito']}Nome: {cores['limpa']}")).strip().title()
média = float(input(f"{cores['azul']}{estilos['negrito']}Média de {cores['vermelho']}{nome}: "))
if média < 5:
    situação = f"{estilos['negrito']}{cores['vermelho']}REPROVADO{cores['limpa']}"
elif média == 6 and média < 7:
    situação = f"{cores['amarelo']}{estilos['negrito']}RECUPERAÇÃO{estilos['reset']}"
else:
    situação = f"{cores['verde']}{estilos['negrito']}APROVADO{estilos['reset']}"

print(f"{cores['cinza']}{estilos['negrito']}Situação do {cores['ciano']}{nome}{cores['cinza']} é igual a {situação}{estilos['reset']}")