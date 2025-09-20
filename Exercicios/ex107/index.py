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
frase = "CASA DE CÂMBIO"

print(f"{estilos['negrito']}{cores['azul']}{"==="*4+"=="}{cores['cinza']}CÂMBIO{cores['verde']}{"==="*5}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 



from modulos import moeda

p = float(input(f"{cores['cinza']}{estilos['negrito']}Digite o preço: {cores['verde']}{estilos['italico']}R$ {estilos['reset']}"))
print(f"{estilos['negrito']}{cores['cinza']}Aumento: {cores['verde']}{moeda.aumentar(p, 10, True)}{estilos['reset']}")
print(f"{estilos['negrito']}{cores['cinza']}Redução: {cores['vermelho']}{moeda.diminuir(p, 13, True)} {estilos['reset']}")
print(f"{estilos['negrito']}{cores['cinza']}Dobro: {cores['amarelo']}{moeda.dobro(p, True)} {estilos['reset']}")
print(f"{estilos['negrito']}{cores['cinza']}Metade: {cores['pretoebranco']}{moeda.metade(p, True)} {estilos['reset']}")

solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")

from modulos import moedas

p = float(input("Digite o Preço: R$"))
print(f"A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}")
print(f"O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}")
print(f"Aumentando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}")
print(f"Diminuindo 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}")