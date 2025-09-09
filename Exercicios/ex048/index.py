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
tabuada = 'TÁBUADA GUANABARA'
print(f"{estilos['negrito']}{cores['ciano']}{"-=" * 28}{estilos['reset']}")
print(f"{estilos['negrito']}{cores['vermelho']}{fundo['verde']}{tabuada.center(55)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"-=" * 28}{estilos['reset']}")


numero = int(input("Digite um número: "))

print(f"{estilos['negrito']}{cores['roxo']}{"---" * 5}{cores['limpa']}")
for i in range(1, 10 + 1):
    print(f"{estilos['negrito']}{numero} x {i} = {numero * i}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['roxo']}{"---" * 5}{cores['limpa']}")