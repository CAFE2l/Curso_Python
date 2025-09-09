 
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
fibo = "Números de Fibonacci"
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*5}{cores['azul']}FIBONACCI{cores['vermelho']}{"==="*5 + "="}{cores['limpa']}")
print(f"{fundo['roxo_claro']}{cores['verde']}{estilos['italico']}{estilos['negrito']}{fibo.center(40)}{cores['limpa']}")
print(f"{cores['vermelho']}{estilos['negrito']}{"==="*13 + "="}{cores["limpa"]}")

n = int(input("Quantos números da sequência de fibonacci você quer mostrar? "))

# primeiros dois termos fixos
t1 = 0
t2 = 1
cont = 0

print("Sequência de Fibonacci:")
while cont < n:   # repete até mostrar n termos
    print(t1, end=f"{estilos['negrito']}{cores['azul']} -> {cores['limpa']}" if cont < n - 1 else "\n")
    t3 = t1 + t2      # próximo termo é a soma dos dois anteriores
    t1 = t2           # amtualiza: o 2º vira o 1º
    t2 = t3           # e o novo termo vira o 2º
    cont += 1

print("Acabou")
