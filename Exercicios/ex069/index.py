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

# Cabeçalho bonito
mercado = "Raspa Preço"
print(f"{estilos['negrito']}{cores['amarelo']}{'==='*5}{cores['vermelho']}MERCADO{cores['amarelo']}{'==='*5+'=='}{estilos['reset']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{estilos['italico']}{mercado.center(39)}{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"==="*13}{estilos['reset']}")

# Variáveis de controle
total = 0 
milao = 0
contador = 0
menor_preco = 0
barato = ""

# Loop principal
while True:
    nome = str(input(f"{estilos['negrito']}{cores['cinza']}Nome do Produto: {estilos['reset']}"))
    preco = float(input(f"{estilos['negrito']}{cores['cinza']}Preço: R${estilos['reset']}"))
    contador += 1
    total += preco

    # Contar produtos acima de 1000
    if preco > 1000:
        milao += 1

    # Verificar mais barato
    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        barato = nome

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

# Saída final com cores
print(f"\n{estilos['negrito']}{cores['verde']}O total da compra foi: R${total:.2f}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}Temos {milao} produto(s) custando mais de R$1000,00{cores['limpa']}")
print(f"{estilos['negrito']}{cores['amarelo']}O produto mais barato foi {barato} que custou R${menor_preco:.2f}{cores['limpa']}")
