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

#Minha solução

pares = 'SOMA DOS PARES'
print(f"{estilos['negrito']}{cores['cinza']}{"-=" * 28}{estilos['reset']}")
print(f"{estilos['negrito']}{cores['amarelo']}{fundo['verde']}{pares.center(55)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['cinza']}{"-=" * 28}{estilos['reset']}")
# Criamos uma variável para acumular a soma dos pares
soma_pares = 0

# Loop para ler 6 números
for i in range(0, 6):
    numero = int(input(f"{estilos["negrito"]}Digite um número: {cores['limpa']}"))
    
    # Verifica se o número é par
    if numero % 2 == 0:
        # Soma o número par à variável acumuladora
        soma_pares += numero

# Exibe o resultado final
print(f"A soma dos números pares é: {soma_pares}")


#Solução do guana
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("Digite o {} valor: ".format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print("Você informou {} números PARES e a soma foi {}".format(cont, soma))