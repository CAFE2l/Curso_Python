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
    "branco": "\033[m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m"
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m"
}
frase = "Vamos Descobrir um Fatorial de um Número"
print(f"{cores['amarelo']}{estilos['negrito']}{"=="*10 + "="}{cores['verde']}FATORIAL{cores['limpa']}{cores['amarelo']}{estilos['negrito']}{"=="*11}{cores['limpa']}")
print(f"{cores['vermelho']}{estilos['italico']}{estilos['negrito']}{frase.center(50)}{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"==="*17}{cores['limpa']}") 
numero = int(input(f"{estilos['negrito']}{cores['ciano']}Digite um número: {cores['limpa']}"))
original = numero
fatorial = 1  # começa em 1 porque é o elemento neutro da multiplicação

while numero > 0:   # enquanto o número for maior que zero
    fatorial *= numero  # multiplica o fatorial pelo número atual
    numero -= 1         # diminui 1 no número

print(f"{estilos['negrito']}{cores['azul']}O fatorial do número {cores['amarelo']}{original} {cores['azul']}é: {cores['vermelho']}{fatorial}{cores['limpa']}")


#Solução do Guaná:

n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end='')
while c > 0:
    print("{}".format(c), end='')
    print(" x " if c > 1 else " = ", end='')
    f = f * c
    c -= 1
print("{}".format(f))