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
frase = "INTERACTIVE HELP SYSTEM"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['cinza']}HELP{cores['verde']}{"==="*5+"="}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 


def ajuda(comando):
    """Função que exibe help de comandos Python"""
    print(f"{cores['cinza']}{estilos['negrito']}Acessando o manual do comando '{cores['vermelho']}{estilos['italico']}{estilos['sublinhado']}{comando}'...{cores['limpa']}")
    print(f"{cores['azul']}{estilos["negrito"]}{"="*50}{estilos['reset']}")
    help(comando)
    print(f"{cores['azul']}{estilos["negrito"]}{"="*50}{estilos['reset']}")

def titulo(txt, simbolo='~'):
    """Função para criar títulos formatados"""
    tamanho = len(txt) + 4
    print(f"{estilos['negrito']}{cores['amarelo']}{simbolo * tamanho}{cores['limpa']}")
    print(f'  {txt}  ')
    print(f"{estilos['negrito']}{cores['amarelo']}{simbolo * tamanho}{cores['limpa']}")

# PROGRAMA PRINCIPAL
titulo(f"{cores['roxo']}{estilos['negrito']}{estilos['italico']}SISTEMA DE HELP PyHELP{cores['limpa']}", '=')

print("""
Este sistema permite consultar o manual de qualquer
comando, função ou biblioteca do Python.

Digite o nome do comando para ver sua documentação.
Digite 'FIM' para encerrar o programa.
""")

while True:
    print("-" * 50)
    comando = input(f"{cores['cinza']}{estilos['negrito']}Função {cores['verde']}ou {cores['cinza']}biblioteca > {cores['limpa']}").strip()
    
    if comando.upper() == 'FIM':
        titulo(f"{cores['vermelho']}{estilos['negrito']}ATÉ LOGO!{estilos['reset']}", '=')
        break
    elif comando == '':
        print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}❌ Digite um comando válido!{estilos['reset']}")
        continue
    else:
        try:
            ajuda(comando)
        except:
             print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}❌ Erro: '{comando}' não foi encontrado!{estilos['reset']}")
             print(f"{estilos['negrito']}{cores['verde']}Verifique se digitou corretamente.{cores['limpa']}")

print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}Programa encerrado.{cores['limpa']}")




solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")



def ajuda(com):
    titulo(f"{fundo['azul']}{cores['cinza']}Acessando o manual do comando '{com}'{cores['limpa']}", '=')
    print(fundo['branco'] + cores['pretoebranco'], end='')
    help(com) 
    print(cores['limpa'], end='')

def titulo(msg, simbolo='~'):
    tam = len(msg) + 4
    
    print(simbolo * tam)
    print(f" {msg}  ")
    print(simbolo * tam)


#Program Principal
comando = ''
while True:
    titulo(f"{fundo['verde']}{cores['cinza']}SISTEMA DE AJUDA PyHELP{cores['limpa']}")
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo(f"{fundo['vermelho']}{cores['cinza']}ATÉ LOGO{cores['limpa']}")