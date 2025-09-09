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
from time import sleep
caixa = "CAXALETRONICO"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5+'=='}{cores['cinza']}cai{cores['amarelo']}X{cores['limpa']}{cores['cinza']}{estilos['negrito']}a{cores['azul']}{'==='*5+'=='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{caixa.center(39)}{estilos['reset']}")
print(f"{cores['azul']}{estilos['negrito']}{"==="*13}{estilos['reset']}")

# Entrada do saque
saque = float(input(f"{cores['pretoebranco']}{estilos['italico']}{estilos['negrito']}Qual o valor a ser sacado? {estilos['reset']}"))

# Valores das cédulas
notas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50]
contadores = {nota: 0 for nota in notas}  # cria um dicionário para contar as notas

total = saque

while total > 0: 
    for nota in notas:
        while total >= nota:
            total -= nota
            contadores[nota] += 1
            print(f"{cores['cinza']}{estilos['negrito']}Dispensando {cores['verde']}R$ {nota},00{estilos['reset']}") 
            sleep(0.15)

# Resultado final
print(f"\n{cores['amarelo']}{estilos['negrito']}Resumo do saque:{estilos['reset']}")
for nota, qtd in contadores.items():
    if qtd > 0:
        print(f"{estilos['negrito']}{cores['vermelho']}{qtd}{cores['azul']} nota(s) de {cores['verde']}R$ {nota},00{estilos['reset']}")

print(f"\n{estilos['italico']}{estilos['sublinhado']}Você sacou um total de{estilos['reset']} {estilos['negrito']}{cores['verde']}R$ {saque:.2f}{estilos['reset']}")