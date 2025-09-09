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

frase = "CADASTRO DE CLT"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5}{cores['cinza']}🪪CLT🪪{cores['azul']}{'==='*6 +'='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['azul']}{estilos['negrito']}{'==='*13}{estilos['reset']}")


nome =  str(input(f"{cores['cinza']}{estilos['negrito']}Nome: "))
anoNascimento = int(input(f"{cores['cinza']}{estilos['negrito']}Ano de Nascimento: "))
carteiraTrabalho = int(input(f"{cores['amarelo']}{estilos['negrito']}Carteira de Trabalho {cores['vermelho']}{estilos['italico']}{estilos['sublinhado']}(0 não tem):{cores['limpa']} "))
anoContratação = int(input(f"{cores['cinza']}{estilos['negrito']}Ano de contratação:{cores['limpa']} ")) if carteiraTrabalho != 0 else 0
salario = float(input(f"{cores['cinza']}{estilos['negrito']}Salário: {estilos['reset']}")) if carteiraTrabalho != 0 else 0
idade = 2025 - anoNascimento
aposentadoria = (anoContratação + 35) - (2025 - idade) if carteiraTrabalho != 0 else 0
print(f"{estilos['negrito']}{cores['vermelho']}{"-="*30}{estilos['reset']}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}Nome: {cores['vermelho']}{nome}{estilos['reset']}") 
print(f"{cores['cinza']}{estilos['negrito']}Idade: {cores['vermelho']}{idade}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['azul']}Carteira de Trabalho: {carteiraTrabalho}{estilos['reset']}")
if carteiraTrabalho != 0:
    print(f"{cores['cinza']}{estilos['negrito']}Ano de contratação: {cores['vermelho']}{anoContratação}{estilos['reset']}")
    print(f"{cores['cinza']}{estilos['negrito']}Salário: {cores['verde']}R$ {salario:.2f}{estilos['reset']}")
    print(f"{cores['cinza']}{estilos['negrito']}Tempo para aposentadoria: {cores['vermelho']}{aposentadoria} anos{estilos['reset']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"-="*30}{cores['limpa']}")