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


converte = "Convertor de Número em Extensos"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5+'=='}{cores['cinza']}EXTENSO{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['azul']}{'==='*5}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{converte.center(39)}{estilos['reset']}")
print(f"{cores['azul']}{estilos['negrito']}{"==="*13}{estilos['reset']}")


valores = []

for cont in range(0, 5):
    try:
        valor = int(input("Digite um valor: "))
        valores.append(valor)
    except ValueError:
        print("Erro: Digite apenas números inteiros!")
        exit()

if valores:  # Verifica se a lista não está vazia
    maior = max(valores)
    menor = min(valores)
    indice_maior = valores.index(maior)
    indice_menor = valores.index(menor)
    print(f"O maior valor foi {maior} na posição {indice_maior} e o menor valor foi {menor} na posição {indice_menor}")
else:
    print("Nenhum valor foi inserido!")