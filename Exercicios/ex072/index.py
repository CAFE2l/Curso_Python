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

placar = "🏆Placar Brasileirão⚽"

print(f"{estilos['negrito']}{cores['vermelho']}{'==='*5+'='}{cores['vermelho']}{cores['cinza']}BRASILEIRÃO{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['azul']}{'==='*5}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{placar.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{"==="*14}{estilos['reset']}")



brasileirão = ('Corithians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', "Flamengo", "Vasco", "Chapecoense", "Atlético", "Botafogo", "Atlético-PR", "Bahia", 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f"{estilos['negrito']}{cores['roxo']}{estilos['italico']}{"-"*22}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['pretoebranco']}{estilos['italico']}5 Primeiros Colocados: {cores['limpa']}")


for cinco in range(0, 5):
    print(f"{cores['verde']}{estilos['negrito']}{cinco+1}ª {cores['cinza']}{brasileirão[cinco]}")
print(f"{estilos['negrito']}{cores['roxo']}{estilos['italico']}{"-"*22}{cores['limpa']}")


print(f"{estilos['negrito']}{cores['azul']}Últimos Colocados:{cores['limpa']} ")
for pos in range(16, 20):  # de 16 até 19 (os 4 últimos)
    print(f"{cores['vermelho']}{estilos['negrito']}{pos+1}ª {cores['cinza']}{brasileirão[pos]}")
print(f"{cores['roxo']}{estilos['negrito']}{estilos['italico']}{"-"*22}{cores['limpa']}")

print(f"{estilos['negrito']}{cores['cinza']}Todos os colocados em ordem alfabética: {cores['limpa']}")

for pos, time in enumerate(sorted(brasileirão), start=1):
    print(f"{cores['amarelo']}{estilos['negrito']}{pos}ª {cores['cinza']}{time}")

print(f"{cores['roxo']}{estilos['negrito']}{estilos['italico']}{"-"*22}{cores['limpa']}")
