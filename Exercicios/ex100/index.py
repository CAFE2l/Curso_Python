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
frase = "ELEIÇÔES 2026"

print(f"{estilos['negrito']}{cores['verde']}{"==="*4+"="}{cores['amarelo']}FAZ_O_L{cores['verde']}{"==="*5}{cores['limpa']}")
print(f"{cores['azul']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['verde']}{"==="*11+"=="}{cores['limpa']}") 


def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if idade < 16:
        return f'{estilos['negrito']}{cores['cinza']}Com {cores['verde']}{idade} {cores['cinza']}anos: {cores['vermelho']}{estilos['italico']}{estilos['sublinhado']}NÃO VOTA.{estilos['reset']}'
    elif 16 <= idade < 65:
        return f'{estilos['negrito']}{cores['cinza']}Com {cores['verde']}{idade} {cores['cinza']}anos: {cores['vermelho']}{estilos['italico']}{estilos['sublinhado']}VOTO OBRIGATÓRIO{estilos['reset']}.'
    else:
        return f'{estilos['negrito']}{cores['cinza']}Com {cores['verde']}{idade} {cores['cinza']}anos: {cores['azul']}{estilos['italico']}VOTO OPCIONAL.{estilos['reset']}'




nascimento = int(input(f'{estilos['negrito']}{cores['cinza']}Em que ano você nasceu? {estilos['reset']}'))
print(voto(nascimento))




solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")



def voto(ano):
    from datetime import date
    atual  = date.today().year
    idade = atual - ano
    if idade < 16:
        return f"com {idade} anos: NÃO VOTA."
    elif 16 <= idade < 18 or idade > 65:
        return f"com {idade} anos: VOTO OPCIONAL."
    else: 
        return f"com {idade} anos: VOTO OBRIGATÓRIO."
#Programa Principal
nasc = int(input("Em que ano você nasceu? "))

print(voto(nasc))
