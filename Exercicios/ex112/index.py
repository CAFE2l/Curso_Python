
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
frase = "LER NÚMEROS INTEIROS E REAIS"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['cinza']}NÚMEROS{cores['verde']}{"==="*4+"="}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 

def leiaInt():
    while True:
        try:
            n = int(input(f'{cores['cinza']}{estilos['negrito']}Digite um número {cores['azul']}inteiro: {cores['limpa']}'))
        except (ValueError, TypeError):
            print(f'{cores['vermelho']}{estilos['italico']}{estilos['negrito']}ERRO! Digite um número inteiro válido.{estilos['reset']}')
            continue
        except (KeyboardInterrupt):
            print(f'\n{cores['vermelho']}{estilos['italico']}O usuário preferiu não digitar esse número.{estilos['reset']}')
            return 0
        else:
            print(f"{cores['cinza']}{estilos['negrito']}O valor digitado pelo usuário foi {cores['verde']}{n}")
            return n 
def leiaFloat():
    while True:
        try:
            n = float(input(f'{cores['cinza']}{estilos['negrito']}Digite um número {cores['amarelo']}real: {cores['limpa']}'))
        except (ValueError, TypeError):
            print(f'{cores['vermelho']}{estilos['italico']}{estilos['negrito']}ERRO! Digite um número real válido.{estilos['reset']}')
            continue
        except(KeyboardInterrupt):
            print(f"{cores['vermelho']}{estilos['italico']}O usuário preferiu não digite o número{estilos['reset']}")
            return 0.0
        else:
            print(f"{cores['cinza']}{estilos['negrito']}O valor digitado pelo usuário foi {cores['verde']}{n}{cores['limpa']}")
            return n

#Progrma Principal 
leiaInt()
leiaFloat()




solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"{cores['vermelho']}{estilos['negrito']}ERRO: por favor, digite um número inteiro válido.{cores['limpa']}")
            continue
        except (KeyboardInterrupt):
            print(f"{cores['vermelho']}{estilos['negrito']}O usuário preferiu não digitar esse número.{cores['limpa']}")
            return 0
        else:
            return n 

num = int(input("Digite um valor: "))
print(f"O valor digitado foi {num}")
