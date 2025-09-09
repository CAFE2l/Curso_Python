from time import sleep
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

print("-=" * 12)
fogos = "FOGOS DO HELL DE JANEIRO"
print(f"{estilos['negrito']}{cores['vermelho']}{fogos.center(20)}{cores['limpa']}")
print("-="*12)

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("🎆FIM🎆")

#Solução do Guaná
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print("Bum! BUM ! PooW!")