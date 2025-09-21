
def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)



def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f"{moeda}{preço:>.2f}".replace('.', ',')


def resumo(preço=0, taxa=10, taxar=5):
    print(f"{'-' * 30}")
    print('RESUMO DO VALOR'.center(30))
    print(f"{'-' * 30}")
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxa}% de desconto: \t{diminuir(preço, taxa, True)}')
    print(f'Com {taxar}% de aumento: \t{aumentar(preço, taxar, True)}')
    print(f"{'-' * 30}")
