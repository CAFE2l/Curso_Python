 
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
    "sem_tachado": "\033[29m"       # Desati    va tachado
}


numeros = []  # lista para guardar os números digitados
frase = "Vários Números Lidos"
print(f"{cores['azul']}{estilos['negrito']}{"==="*5}VARIOS{"==="*5}{estilos['reset']}")
print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{fundo['roxo']}{frase.center(35)}{estilos['reset']}")
print(f"{cores['azul']}{estilos['negrito']}{"==="*12}")

while True:  
    numero = int(input(f"{cores['amarelo']}{estilos['italico']}{estilos['negrito']}{"Digite um número: "}{estilos['reset']}"))

    numeros.append(numero)  # adiciona o número na lista

    continuar = input(f"{estilos['negrito']}Quer continuar {cores['vermelho']}[S/N]: {estilos['reset']}").strip().upper()
    if continuar == "N":  # se digitar N, sai do loop
        break

# Cálculos após sair do loop
soma = sum(numeros)
quantidade = len(numeros)
media = soma / quantidade
maior = max(numeros)
menor = min(numeros)

print(f"A média dos números foi {estilos['negrito']}{estilos['italico']}{cores['vermelho']}{media:.2f}{cores['limpa']}, o maior número foi {estilos['negrito']}{estilos['italico']}{cores['vermelho']}{maior}{cores['limpa']} e o menor número foi {estilos['negrito']}{estilos['italico']}{cores['vermelho']}{menor}{cores['limpa']}")

