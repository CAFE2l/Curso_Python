# PROGRAMA COM LISTA E DUAS FUNÇÕES
# Lista para guardar os números sorteados
# Dicionários para cores e estilos (igual ao original)
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
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m"
}
frase = "SORTEIO DE NÚMEROS"

print(f"{estilos['negrito']}{cores['vermelho']}{"==="*4+"=="}{cores['cinza']}LISTA{cores['azul']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['verde']}{"==="*11+"=="}{cores['limpa']}") 



from random import randint

numeros = []  # Lista vazia para receber os números

def sorteia():
    """Função que sorteia 5 números e coloca na lista"""
    print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}Sorteando 5 números...{estilos['reset']}")
    
    for i in range(5):
        numero_sorteado = randint(1, 10)  # Sorteia número de 1 a 10
        numeros.append(numero_sorteado)   # Adiciona na lista
        print(f"{cores['cinza']}{estilos['negrito']}Sorteei o número: {cores['vermelho']}{estilos['italico']}{estilos['sublinhado']}{numero_sorteado}{estilos['reset']}")
    
    print(f"{cores['cinza']}{estilos['negrito']}Lista completa: {cores['verde']}{estilos['italico']}{numeros}{estilos['reset']}")

def somaPar():
    """Função que soma apenas os números PARES da lista"""
    soma = 0
    pares_encontrados = []
    
    print(f"{cores['cinza']}{estilos['italico']}\nVerificando números pares...{estilos['reset']}")
    
    for numero in numeros:
        if numero % 2 == 0:  # Se for par
            print(f"{cores['cinza']}{estilos['negrito']}O número {cores['amarelo']}{numero} {cores['cinza']}é {cores['verde']}PAR{estilos['reset']}")
            soma += numero
            pares_encontrados.append(numero)
        else:
            print(f"{cores['cinza']}{estilos['negrito']}O número {cores['amarelo']}{numero} {cores['cinza']}é {cores['vermelho']}ÍMPAR{estilos['reset']}")
    
    print(f"{cores['cinza']}{estilos['negrito']}Números {cores['verde']}pares {cores['cinza']}encontrados: {cores['vermelho']}{pares_encontrados}{estilos['reset']}")
    print(f"{cores['cinza']}{estilos['negrito']}Soma dos {cores['verde']}pares: {cores['roxo']}{soma}{estilos['reset']}")

# PROGRAMA PRINCIPAL
print("="*40)
print("PROGRAMA SORTEIA E SOMA PARES")
print("="*40)

# Chama a primeira função
sorteia()

# Chama a segunda função
somaPar()




solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")

from random import randint
from time import sleep

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f"{n} ", end='', flush=True)
        sleep(0.3)
    print("PRONTO!")

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}")


numeros = list()
sorteia(numeros)
somaPar(numeros)

print("="*40)