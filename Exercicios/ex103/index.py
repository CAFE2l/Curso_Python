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
frase = "DIGITE NÚMERO INTEIRO VAGABUNDO"

print(f"{estilos['negrito']}{cores['azul']}{"==="*4+"="}{cores['cinza']}INTEIRO{cores['verde']}{"==="*5}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 



def leiaint():
    while True:
        try:
            n = int(input(f'{cores['cinza']}{estilos['negrito']}Digite um número: {cores['limpa']}'))
        except (ValueError, TypeError):
            print(f'{cores['vermelho']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}ERRO! Digite um número inteiro válido.{cores['limpa']}')
            continue
        except KeyboardInterrupt:
            print(f'{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}Entrada de dados interrompida pelo usuário.{estilos['reset']}')           
            return 0
        else:
            return n



leiaint()