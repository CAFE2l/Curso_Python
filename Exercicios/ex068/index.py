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
    "duplosublinhado": "\033[21m",  # Sublinhado duplo
    "normal": "\033[22m",           # Desativa negrito e fraco
    "semitalico": "\033[23m",       # Desativa itálico
    "sem_sublinhado": "\033[24m",   # Desativa sublinhado
    "sem_inverso": "\033[27m",      # Desativa inverso
    "visivel": "\033[28m",          # Desativa invisível
    "sem_tachado": "\033[29m"       # Desativa tachado
}
nomes = []
idades = []
sexos = []
pessoa = "CADASTRE UMA PESSOA"

print(f"{estilos['negrito']}{cores['amarelo']}{'==='*5}{cores['vermelho']}{'CADASTRO'}{cores['amarelo']}{'==='*5+'='}{estilos['reset']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{estilos['italico']}{pessoa.center(39)}{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"==="*13}{estilos['reset']}")
info = "Passe as informações"

while True:
    print(f"{cores['ciano']}{estilos['negrito']}{"---"*13}{estilos['reset']}")
    print(f"{cores['roxo']}{estilos['negrito']}{estilos['italico']}{fundo['vermelho_claro']}{info.center(39)}{estilos['reset']}")
    print(f"{cores['ciano']}{estilos['negrito']}{"---"*13}{estilos['reset']}")
    nomes.append(input(f"{cores['ciano']}{estilos['negrito']}Digite seu nome: {estilos['reset']}"))
    idades.append(int(input(f"{cores['azul']}{estilos['negrito']}Digite sua idade: {estilos['reset']}")))
    sexos.append(input(f"{cores['azul']}{estilos['negrito']}{estilos['negrito']}Digite seu sexo (M/F): {estilos['reset']}").upper())
    continuar = input(f"{estilos['sublinhado']}Deseja continuar?{estilos['reset']} {cores['vermelho']}{estilos['negrito']}{estilos['italico']}(S/N): {estilos['reset']}").upper()
    if continuar == "N":
        break

# Quantas pessoas têm mais de 18 anos
maiores = sum(1 for idade in idades if idade > 18)
print(f"{estilos['negrito']}Pessoas maiores de {cores['vermelho']}18: {estilos['reset']}{cores['amarelo']}{estilos['negrito']}{maiores}{estilos['reset']}")

# Quantos homens foram cadastrados
homens = sum(1 for s in sexos if s == "M")
print(f"Ao todo temos {cores['vermelho']}{estilos['negrito']}{homens}{estilos['reset']} {cores['ciano']}{estilos['negrito']}{estilos['sublinhado']}homens cadastrados{estilos['reset']}")

# Quantas mulheres têm menos de 20 anos
mulheres_menos_20 = sum(1 for i, s in zip(idades, sexos) if s == "F" and i < 20)
print(f"E temos {estilos['negrito']}{cores['vermelho']}{mulheres_menos_20} mulheres com menos de 20 anos{estilos['reset']}")

