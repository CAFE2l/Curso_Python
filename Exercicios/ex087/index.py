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

frase = "🎯💸MEGA-SENA🪙🎯"

print(f"{estilos['negrito']}{cores['verde']}{'==='*5}{cores['amarelo']}📠MEGA-SENA💰{cores['verde']}{'==='*4+'=='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{'==='*14}{estilos['reset']}")


jogos = int(input(f"{cores['cinza']}{estilos['negrito']}Quantos jogos você quer que eu sorteie? {cores['limpa']}"))
print(f"{cores['roxo']}{estilos['negrito']}{'-=' * 15}sorteando {jogos} jogos{'-=' * 15}{cores['limpa']}")
from random import sample
from time import sleep      
for jogo in range(0, jogos):
    print(f"{cores['amarelo']}{estilos['negrito']}Jogo {jogo + 1}: {cores['verde']}{sorted(sample(range(1, 61), 6))}{cores['limpa']}")
    sleep(1)
print(f"{cores['roxo']}{estilos['negrito']}{'-=' * 15}{cores['verde']}BÁ SORTE :D{cores['roxo']}{'-=' * 15}{cores['limpa']}")
