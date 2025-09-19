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
frase = "FICHA DO JOGADOR"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['cinza']}FICHA{cores['verde']}{"==="*5}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 

def ficha(nome="<desconhecido>", gols=0):
    """
    Mostra a ficha do jogador
    
    Parâmetros opcionais:
    nome: nome do jogador (padrão: "<desconhecido>")
    gols: quantidade de gols (padrão: 0)
    """
    print(f"{cores['cinza']}{estilos['negrito']}O jogador {cores['vermelho']}{nome}{cores['cinza']} fez {cores['verde']}{gols} {cores['cinza']}gol(s) no campeonato.")

# Coleta dados do usuário
nome = input(f"{cores['cinza']}{estilos['negrito']}Nome do jogador: ").strip()
gols_input = input(f"{cores['cinza']}{estilos['negrito']}Número de gols: {estilos['reset']}").strip()

# Processa o nome
if nome == "":
    nome = None  # Usa valor padrão

# Processa os gols
if gols_input == "":
    gols = None  # Usa valor padrão
elif gols_input.isnumeric():
    gols = int(gols_input)
else:
    print(f"{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}{cores['vermelho']}Número inválido! Usando 0.{estilos['reset']}")
    gols = None  # Usa valor padrão

# Chama a função conforme os dados informados

if nome and gols is not None:
    # Tem nome E gols
    ficha(nome, gols)
elif nome:
    # Só tem nome
    ficha(nome)
elif gols is not None:
    # Só tem gols
    ficha(gols=gols)
else:
    # Não tem nada
    ficha()

print(f"{estilos['negrito']}{cores['amarelo']}{"="*50}{estilos['reset']}")


solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")

#Programa Principal 
def ficha(jog="<desconhecido>", gol=0):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")

n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))

if g.isnumeric():
    g = int(g)
else: 
    g = 0

if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n, g)
