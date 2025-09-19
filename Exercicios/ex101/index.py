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
frase = "FATORIAL DE UM NÚMERO"

print(f"{estilos['negrito']}{cores['vermelho']}{"==="*4}{cores['cinza']}FATORIAL{cores['azul']}{"==="*5}{cores['limpa']}")
print(f"{cores['azul']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['verde']}{"==="*11+"=="}{cores['limpa']}") 

def fatorial(numero=None, show=None):
    # Se não passou parâmetros, pede pro usuário
    if numero is None:
        numero = int(input(f"{cores['cinza']}{estilos['negrito']}{estilos['italico']}Digite um número: "))
    if show is None:
        show = input(f"{cores['cinza']}{estilos['negrito']}{estilos['italico']}Quer ver o cálculo? {cores['vermelho']}{estilos['sublinhado']}(s/n):{cores['limpa']} ") == 's'
    
    f = 1
    for c in range(numero, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(f' {cores['verde']}{estilos['negrito']}x{estilos['reset']} ', end='')
            else:
                print(f' = {cores['vermelho']}{estilos['negrito']}{f}{estilos['reset']}')
    return f

# Pode usar das duas formas:
fatorial()        # Pede pro usuário
fatorial(5, True) # Ou passa direto