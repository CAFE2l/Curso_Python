def moeda(valor):
    return f"R$ {valor:.2f}".replace('.', ',')

def aumentar(preço, taxa, formato=True):
    res = preço + (preço * taxa / 100)
    return moeda(res) if formato else res

def diminuir(preço, taxa, formato=True):
    res = preço - (preço * taxa / 100)
    return moeda(res) if formato else res

def dobro(preço, formato=True):
    res = preço * 2
    return moeda(res) if formato else res

def metade(preço, formato=True):
    res = preço / 2
    return moeda(res) if formato else res