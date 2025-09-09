# Dicionários de estilos, cores e fundo
cores = {
    "limpa": "\033[m", 
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m", 
    "azul": "\033[34m", 
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
    "pretoebranco": "\033[7;30m"
}

fundo  = {
    "branco": "\033[m", 
    "vermelho": "\033[41m",
    "verde": "\033[42m",
    "amarelo": "\033[43m", 
    "azul": "\033[44m", 
    "roxo": "\033[45m",
    "ciano": "\033[46m",
    "cinza": "\033[47m"   
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

# Programa para verificar se um número é primo

numero = int(input("Digite um número inteiro: "))

# Contador de divisores
divisores = 0

# Testa todos os números de 1 até o próprio número
for i in range(1, numero + 1):
    if numero % i == 0:  # se não sobrar resto, é divisor
        divisores += 1

# Se tiver exatamente 2 divisores (1 e ele mesmo), é primo
if divisores == 2:
    print(f"{numero} é primo.")
else:
    print(f"{numero} NÃO é primo.")

#Solução do guaná
num = int(input("Digite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')  
        tot += 1 
    else:
        print('\033[31m', end='')
    print("{} ".format(c), end='')
print("\n\033[mO número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("E por isso ele É PRIMO!")
else: 
    print("E por isso ele NÃO É PRIMO")