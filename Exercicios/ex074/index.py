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

frase = "Também não sei o que escrever aqui >:("

print(f"{estilos['negrito']}{cores['vermelho']}{'==='*5+'=='}{cores['vermelho']}{cores['cinza']}NÚMEROS{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['azul']}{'==='*6}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{'==='*14}{estilos['reset']}")
# Ler os 4 números
n1 = int(input(f"{estilos['negrito']}{cores['azul']}Digite um número: "))
n2 = int(input(f"{estilos['negrito']}{cores['azul']}Digite outro número: "))
n3 = int(input(f"{estilos['negrito']}{cores['azul']}Digite mais um número: "))
n4 = int(input(f"{estilos['negrito']}{cores['azul']}Digite o último número: {estilos['reset']}"))

# Guardar em uma tupla
numeros = (n1, n2, n3, n4)

# Contar quantas vezes o número 9 aparece
qtd = numeros.count(9)

#Números pares
pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f"Números {cores['amarelo']}{estilos['negrito']}pares{estilos['reset']} digitados: {estilos['negrito']}{cores['vermelho']}{pares}{cores['limpa']}")
else:
    print(f"{cores['vermelho']}{estilos['negrito']}Nenhum número par foi digitado.{cores['limpa']}")

#posição do 3
if 3 in numeros:
    tres = numeros.index(3)
    print(f"{cores['cinza']}{estilos['negrito']}O número {cores['amarelo']}3{cores['limpa']}{estilos['negrito']}{cores['cinza']} foi digitado na {cores['verde']}{tres + 1}ª posição.{cores['limpa']}")
else:
    print(f"{cores['vermelho']}{estilos['negrito']}O número 3 não foi digitado.")

# Mostrar resultado
if qtd == 1:
    print(f"{cores['cinza']}{estilos['negrito']}O número {cores['amarelo']}9{cores['limpa']} foi digitado {cores['verde']}{qtd} vez.{estilos['reset']}")
elif qtd > 1:
    print(f"{cores['cinza']}{estilos['negrito']}O número {cores['amarelo']}9{cores['limpa']} foi digitado {cores['verde']}{qtd} vezes.{estilos['reset']}")      
else:
    print(f"{estilos['negrito']}{cores['vermelho']}O número 9 não foi digitado.{estilos['reset']}")
