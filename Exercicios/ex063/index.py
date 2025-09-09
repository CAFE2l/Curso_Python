 
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

# Inicializando as variáveis
soma = 0
quantidade = 0
numero = 0
text = "Contador de Número no Teclado com Pause"
print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['vermelho']}CONTADOR{cores['azul']}{"==="*5 + "="}{cores['limpa']}")
print(f"{fundo['verde_claro']}{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{text.center(30)}{cores['limpa']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"==="*13}{cores['limpa']}")

# Loop principal para leitura dos números
while numero != 999:
    numero = int(input(f"{estilos['negrito']}Digite um número inteiro {cores['vermelho']}{estilos['italico']}(999 para parar o programa): {cores['limpa']}"))
    
    # Verifica se o número não é a condição de parada
    if numero != 999:
        soma += numero  # Adiciona o número à soma
        quantidade += 1  # Conta mais um número
    
# Exibe os resultados
print(f"Você digitou {cores['amarelo']}{estilos['negrito']}{quantidade} números.{estilos['reset']}")
print(f"A soma entre eles é {estilos['negrito']}{cores['amarelo']}{soma}.{cores['limpa']}")