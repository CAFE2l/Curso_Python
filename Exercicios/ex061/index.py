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



print(f"{estilos['negrito']}{cores['azul']}{"==" * 5 }{cores['vermelho']}RAZÃO{cores['azul']}{"==" * 5}{cores['limpa']}")
menu = "Razão de uma PA"
print(f"{estilos['negrito']}{estilos['italico']}{fundo['roxo']}{cores['amarelo']}{menu.center(25)}{cores['limpa']}")
print(f"{cores['azul']}{estilos['negrito']}{"==="*8 + "="}{cores['limpa']}")
# Lê o primeiro termo e a razão da PA

primeiro = int(input(f"{estilos['negrito']}{estilos['italico']}Primeiro termo: {estilos['reset']}"))
razao = int(input(f"{estilos['negrito']}{estilos['italico']}Razão: {estilos['reset']}"))

# Inicializa variáveis de controle
termo = primeiro   # termo atual da PA
cont = 0           # quantos termos já mostramos

# Loop: mostra exatamente 10 termos
while cont < 10:
    # imprime o termo e coloca ' -> ' até o penúltimo;
    # no último termo, quebra a linha
    print(f"{cores['pretoebranco']}{estilos['italico']}{termo}{cores['limpa']}", end=f"{cores['azul']}{estilos['negrito']} -> {cores['limpa']}" if cont < 9 else "\n")

    termo += razao   # próximo termo da PA
    cont += 1        # incrementa o contador

termos = 0 
print("Quer continuar? [S/N]: ")
resposta = str(input("Escolha:")).upper()

if resposta == "S":
    termos = int(input("Você quer mostrar mais quantos termos? "))
    total = cont + termos
    while cont < total:
        print(f"{cores['pretoebranco']}{estilos['italico']}{termo}{cores['limpa']}", end=f"{cores['azul']}{estilos['negrito']} -> {cores['limpa']}" if cont < total - 1 else "\n")
        termo += razao   # próximo termo da PA
        cont += 1        # incrementa o contador
else: 
    print(f"{cores['amarelo']}{estilos['negrito']}FIM")



print(f"{cores['amarelo']}{estilos['negrito']}⭐Acabou🎉{cores['limpa']}")

#Solução do guaná
print("Gerador de PA")
print("=-" * 10)
primeiro = int(input("Primeiro Termo: "))
razão = int(input("Razão da PA:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("progressão finalizada com {} termos mostrados".format(total))