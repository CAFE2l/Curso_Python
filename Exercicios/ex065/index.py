 
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
somador = "SOMADOR DE NÚMEROS"

print(f"{cores['vermelho']}{estilos['negrito']}{"==="*5}{cores['amarelo']}{"SOMADOR"}{cores['vermelho']}{"===="*4 + "="}{estilos['reset']}")
print(f"{estilos['negrito']}{cores['verde']}{fundo['branco']}{estilos['italico']}{somador.center(39)}{estilos['reset']}")
print(f"{estilos['negrito']}{cores['azul']}{'==='*13}{estilos['reset']}")

n = s = 0
count = 0
while True:
    n = int(input(f"{estilos['negrito']}{cores['ciano']}Digite um número {estilos['italico']}{cores['vermelho']}(999 para sair):{cores['ciano']}{estilos['reset']}"))
    if n == 999:
        break
    s += n
    count += 1
print(f"{cores['verde']}{estilos['negrito']}A soma dos {cores['amarelo']}{estilos['italico']}{count}{estilos['reset']}{cores['verde']} {estilos['negrito']}valores foi {cores['amarelo']}{estilos['negrito']}{estilos['italico']}{s}.{estilos['reset']}")
