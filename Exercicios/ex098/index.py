# Dicionários para cores e estilos (igual ao original)
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
frase = "ANALISADOR DE VALORES"

print(f"{estilos['negrito']}{cores['vermelho']}{"==="*4+"=="}{cores['cinza']}VALUES{cores['azul']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['verde']}{"==="*11+"=="}{cores['limpa']}") 

def maior(valores):
    print(f"{cores['cinza']}{estilos['negrito']}Os valores informados foram: {cores['limpa']}", end=" ")
    for valor in valores:
        print(f"{cores['verde']}{estilos['negrito']}{estilos['italico']}{valor}{cores['limpa']}", end=' ')
    print(f"{cores['cinza']}{estilos['negrito']}Ao todo foram passados {cores['vermelho']}{estilos['italico']}{estilos['sublinhado']}{len(valores)}{estilos['reset']} {cores['cinza']}valores")
    print(f"{cores['cinza']}{estilos['negrito']}O {cores['verde']}maior{cores['cinza']} valor informado foi: {cores['vermelho']}{estilos['sublinhado']}{estilos['italico']}{max(valores)}{estilos['reset']}")


maior(valores=(1,2,3,4, 5, 6, 7, 80))