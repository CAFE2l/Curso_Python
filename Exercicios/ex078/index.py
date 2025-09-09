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

numeros = []


lista = "Listinhas de Números >:D"

print(f"{estilos['negrito']}{cores['vermelho']}{'==='*5+'=='}{cores['verde']}LISTA{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['azul']}{'==='*5 + "=="}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['roxo']}{fundo['branco']}{lista.center(39)}{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"==="*13}{estilos['reset']}")

while True:
    numero = int(input(f"{estilos['negrito']}{cores['azul']}{estilos['sublinhado']}Digite um número: {estilos['reset']}"))
    
    if numero in numeros:
        print(f"{cores['cinza']}Valor duplicado! {estilos['negrito']}{cores['vermelho']}Não vou adicionar >:(")
    else:
        numeros.append(numero)
        print(f"{cores['cinza']}Valor adicionado com {estilos['negrito']}{cores['verde']}sucesso {estilos['reset']}{cores['cinza']}:){estilos['reset']}")
    
    if input(f"{cores['cinza']}{estilos['negrito']}Deseja continuar? {cores['amarelo']}[S/N]{cores['limpa']} ").strip().upper() != 'S':
        break

print(f"{cores['roxo']}{estilos['negrito']}Você digitou os valores {cores['vermelho']}{estilos['italico']}{numeros}{estilos['reset']}")