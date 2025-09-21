
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

preço = float(input(f'{cores["cinza"]}{estilos["negrito"]}Digite o preço: {cores["verde"]}{estilos["italico"]}R${estilos["reset"]}'))
taxa = int(input(f'{cores["cinza"]}{estilos["negrito"]}Digite um valor para a taxa aplicada: {cores["verde"]}{estilos["italico"]}{estilos["reset"]}'))



def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)



def resumo():
    print(f"{cores['amarelo']}{estilos['negrito']}{'-' * 30}{cores['limpa']}")
    print(f'{cores['vermelho']}{estilos['negrito']}RESUMO DO VALOR{cores['limpa']}'.center(30))
    print(f"{cores['amarelo']}{estilos['negrito']}{'-' * 30}{cores['limpa']}")
    print(f'{estilos['negrito']}{cores['cinza']}Preço analisado: {cores['verde']}\t{moeda(preço)}')
    print(f'{estilos['negrito']}{cores['cinza']}Dobro do preço: {cores['amarelo']}\t{dobro(preço, True)}')
    print(f'{estilos['negrito']}{cores['cinza']}Metade do preço: {cores['roxo']}\t{metade(preço, True)}')
    print(f'{estilos['negrito']}{cores['cinza']}Com {taxa}% de desconto: {cores['verde']}\t{diminuir(preço, taxa, True)}')
    print(f'{estilos['negrito']}{cores['cinza']}Com {taxa}% de aumento: {cores['vermelho']}\t{aumentar(preço, taxa, True)}')
    print(f"{cores['amarelo']}{estilos['negrito']}{'-' * 30}{cores['limpa']}")
def moeda(preço=0, simbolo='R$'):
    return f"{simbolo} {preço:.2f}".replace('.', ',')

def leiaDinheiro(msg="Digite o preço: R$ "):
    while True:
        try:
            valor = float(input(msg).strip().replace(',', '.'))
            return valor
        except ValueError:
            print("ERRO: Valor inválido!")

def leiaTaxa(msg="Digite a taxa (%): "):
    while True:
        try:
            taxa = float(input(msg).strip())
            return taxa
        except ValueError:
            print("ERRO: Taxa inválida!")

def aumentar(preço=0, taxa=0, formato=True):
    res = preço + (preço * taxa / 100)
    return moeda(res) if formato else res
