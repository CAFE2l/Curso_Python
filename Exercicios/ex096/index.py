# Dicionários para cores e estilos (igual ao original)
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
terreno = "ESCREVA UMA FRASE"

print(f"{estilos['negrito']}{cores['vermelho']}{"==="*5}{cores['cinza']}FRASE{cores['azul']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{terreno.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['verde']}{"==="*11+"=="}{cores['limpa']}")


def escreva(texto):

    # Calcula o tamanho do texto + 4 espaços (2 de cada lado)
    tamanho = len(texto) + 4
    
    # Imprime a linha superior
    print(f"{cores['vermelho']}{'~' * tamanho}{cores['limpa']}")
    
    # Imprime o texto centralizado com 2 espaços de cada lado
    print(f'{estilos['negrito']}{estilos['italico']}  {texto}  {estilos['reset']}')
    
    # Imprime a linha inferior
    print(f"{cores['azul']}{'~' * tamanho}{cores['limpa']}")


# --- Programa Principal ---


# Você também pode pedir para o usuário digitar:
frase_usuario = str(input(f"{cores['cinza']}{estilos['negrito']}Escreva uma frase qualquer: {estilos['reset']}"))
escreva(frase_usuario)


solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f"  {msg}  ")
    print('~'*tam)

#programa principal
escreva('gustavo guanabara')
escreva('curso de python no youtube')
escreva('CeV')