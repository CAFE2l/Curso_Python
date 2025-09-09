# Dicionários de cores, fundos e estilos
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

# Função para criar linha decorativa
def linha(texto="", cor=cores['limpa'], estilo=estilos['reset'], largura=30):
    print(f"{estilo}{cor}{texto.center(largura, '=')}{estilos['reset']}")

# Função para mostrar título
def titulo(texto):
    print(f"{estilos['negrito']}{cores['amarelo']}{'='*30}{estilos['reset']}")
    print(f"{estilos['negrito']}{cores['roxo']}{fundo['ciano']}{texto.center(30)}{cores['limpa']}")
    print(f"{estilos['negrito']}{cores['amarelo']}{'='*30}{estilos['reset']}")

# Programa principal
titulo("Descobridor de SEXO")

# Validação do sexo
while True:
    sexo = input(f"Digite seu sexo {estilos['negrito']}[M/F]: {estilos['reset']}").strip().upper()
    if sexo in ["M", "F"]:
        break
    print(f"{cores['vermelho']}{estilos['negrito']}Digite apenas M ou F!{estilos['reset']}")

linha("Resultado", cor=cores['ciano'], estilo=estilos['negrito'])

if sexo == "F":
    print(f"{estilos['negrito']}O sexo fornecido foi {cores['vermelho']}Feminino{estilos['reset']}")
else:
    print(f"{estilos['negrito']}O sexo fornecido foi {cores['azul']}Masculino{estilos['reset']}")
    
linha("", cor=cores['amarelo'], estilo=estilos['negrito'])
