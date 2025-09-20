def moeda(valor):
    """
    Formata um valor como moeda brasileira
    Parâmetro: valor (float) - valor a ser formatado
    Retorna: string no formato "R$ XX,XX"
    """
    return f"R$ {valor:.2f}".replace('.', ',')

def aumentar(preço, taxa, formato=True):
    """
    Calcula aumento percentual no preço
    
    Parâmetros:
    - preço (float): valor original
    - taxa (float): percentual de aumento
    - formato (bool): True = retorna formatado, False = retorna número
    
    Retorna: string formatada OU float, dependendo do parâmetro 'formato'
    """
    res = preço + (preço * taxa / 100)
    return moeda(res) if formato else res

def diminuir(preço, taxa, formato=True):
    """
    Calcula redução percentual no preço
    
    Parâmetros:
    - preço (float): valor original  
    - taxa (float): percentual de redução
    - formato (bool): True = retorna formatado, False = retorna número
    
    Retorna: string formatada OU float, dependendo do parâmetro 'formato'
    """
    res = preço - (preço * taxa / 100)
    return moeda(res) if formato else res

def dobro(preço, formato=True):
    """
    Calcula o dobro do preço
    
    Parâmetros:
    - preço (float): valor original
    - formato (bool): True = retorna formatado, False = retorna número
    
    Retorna: string formatada OU float, dependendo do parâmetro 'formato'
    """
    res = preço * 2
    return moeda(res) if formato else res

def metade(preço, formato=True):
    """
    Calcula a metade do preço
    
    Parâmetros:
    - preço (float): valor original
    - formato (bool): True = retorna formatado, False = retorna número
    
    Retorna: string formatada OU float, dependendo do parâmetro 'formato'
    """
    res = preço / 2
    return moeda(res) if formato else res