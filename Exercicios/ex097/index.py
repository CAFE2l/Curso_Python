# PROGRAMA CONTADOR - VERSÃO SIMPLES
# Exercício: função contador() com 3 parâmetros
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
terreno = "CONTADOR DE 3 PARÂMETROS"

print(f"{estilos['negrito']}{cores['vermelho']}{"==="*4}{cores['cinza']}CONTADOR{cores['azul']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{terreno.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['verde']}{"==="*11+"=="}{cores['limpa']}")


def contador(inicio, fim, passo):
    """Função que faz contagem com os parâmetros dados"""
    
    if inicio < fim:
        # Contagem crescente
        atual = inicio
        while atual <= fim:
            print(atual, end=' ')
            atual += passo
        print(f'{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}FIM!{estilos['reset']}')
    else:
        # Contagem decrescente
        atual = inicio
        while atual >= fim:
            print(atual, end=' ')
            atual -= passo
        print(f'{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}FIM!{estilos['reset']}')

# PROGRAMA PRINCIPAL

# a) de 1 até 10, de 1 em 1
print(f"{cores['cinza']}{estilos['negrito']}Contagem de {cores['verde']}1{cores['cinza']} até {cores['verde']} {cores['verde']}10 {cores['cinza']}de  {cores['verde']}1 {cores['cinza']}em  {cores['verde']}1:")
contador(1, 10, 1)

# b) de 10 até 0, de 2 em 2
print(f"\n{cores['cinza']}{estilos['negrito']}Contagem de {cores['vermelho']}10 {cores['cinza']}até  {cores['vermelho']}0 {cores['cinza']}de  {cores['vermelho']}2{cores['cinza']} em  {cores['vermelho']}2:")
contador(10, 0, 2)

# c) uma contagem personalizada
print(f"\n{cores['roxo']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}Contagem personalizada{cores['limpa']}")
inicio = int(input(f"{cores['cinza']}{estilos['negrito']}Digite o início:{cores['limpa']} "))
fim = int(input(f"{cores['cinza']}{estilos['negrito']}Digite o fim: {cores['limpa']}"))
passo = int(input(f"{cores['cinza']}{estilos['negrito']}Digite o passo: {cores['limpa']}"))
contador(inicio, fim, passo)



solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-='*20)
    print(f"contagem de {i} ate {f} de {p} em {p}")
    sleep(2.5)

   


    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= p 
        print("FIM!")




#programa principal:
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))
contador(ini, fim, pas)