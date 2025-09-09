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

gordo = "QUEM É O LUÍS🫃"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5}{cores['cinza']}LUIS{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['vermelho']}{'==='*7}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['roxo']}{fundo['branco']}{gordo.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{'==='*13+'='}{estilos['reset']}")

pessoas = []

while True:
    nome = str(input(f"{estilos['negrito']}{cores['azul']}Nome: {cores['limpa']}"))
    peso = int(input(f"{estilos['negrito']}{cores['azul']}Peso: {cores['limpa']}"))
    
    pessoas.append([nome, peso])

    resp = str(input(f"{cores['cinza']}{estilos['negrito']}Quer continuar? {cores['vermelho']}{estilos['sublinhado']}{estilos['italico']}[S/N]{estilos['reset']} ")).strip().upper()[0]
    if resp in 'Nn':
        break

# CORREÇÃO PRINCIPAL: Encontrar maior e menor peso usando key=lambda
pessoa_maior_peso = max(pessoas, key=lambda x: x[1])  # Compara pelo peso (índice 1)
pessoa_menor_peso = min(pessoas, key=lambda x: x[1])  # Compara pelo peso (índice 1)

print(f"{cores['cinza']}{estilos['negrito']}Ao todo, você cadastrou {cores['amarelo']}{len(pessoas)}{cores['cinza']} pessoas.")
print(f"O maior peso foi de {cores['verde']}{pessoa_maior_peso[1]}Kg{cores['cinza']} peso de {cores['roxo']}{pessoa_maior_peso[0]}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}O menor peso foi de {cores['vermelho']}{pessoa_menor_peso[1]}Kg{cores['cinza']} peso de {cores['roxo']}{pessoa_menor_peso[0]}{estilos['reset']}")

# ALTERNATIVA: Usando apenas os pesos para comparação
# pesos = [pessoa[1] for pessoa in pessoas]
# maior_peso = max(pesos)
# menor_peso = min(pesos)
# 
# # Encontrar as pessoas com esses pesos
# pessoa_maior = next(pessoa for pessoa in pessoas if pessoa[1] == maior_peso)
# pessoa_menor = next(pessoa for pessoa in pessoas if pessoa[1] == menor_peso)  