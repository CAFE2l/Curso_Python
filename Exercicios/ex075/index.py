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

produtos = ("Dokolokotele", 1,
            "Melitrele", 3.54,
            "Alitrepe", 2.99,
            "Zeltrone", 4.99,
            "Caletrona", 5.99)

print(f"{estilos['negrito']}{cores['azul']}{"="*20}{cores['cinza']}{"PREÇOS"}{cores['vermelho']}{"="*20}{estilos['reset']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{'LISTAGEM DE PREÇOS':^45}{cores['limpa']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"="*46}{estilos['reset']}")

for i in range(0, len(produtos), 2):  # vai de 2 em 2
    nome = produtos[i]
    preco = produtos[i+1]
    print(f"{cores['cinza']}{estilos['negrito']}{nome:.<30}{cores['verde']}R${preco:>7.2f}{cores['limpa']}")  # tabulação bonitinha
print(f"{cores['amarelo']}{estilos['negrito']}{"="*42}{estilos['reset']}")
