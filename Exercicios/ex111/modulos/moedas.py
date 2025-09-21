
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
def leiaDinheiro(msg="Digite o preço: R$ "):
    """Função que LÊ e RETORNA um valor monetário"""
    while True:
        try:
            entrada = input(f'{cores["cinza"]}{estilos["negrito"]}{msg}{cores["verde"]}{cores["limpa"]}')
            valor = float(entrada.strip().replace(',', '.'))
            if valor < 0:
                print(f'{cores["vermelho"]}{estilos["negrito"]}ERRO: Valor não pode ser negativo!{cores["limpa"]}')
                continue
            return valor  # ← RETORNA o valor lido
        except ValueError:
            print(f'{cores["vermelho"]}{estilos["negrito"]}ERRO: Digite um valor válido!{cores["limpa"]}')

def leiaTaxa(msg="Digite a taxa (%): "):
    """Função que LÊ e RETORNA uma taxa"""
    while True:
        try:
            entrada = input(f'{cores["cinza"]}{estilos["negrito"]}{msg}{cores["verde"]}{cores["limpa"]}')
            taxa = float(entrada.strip())
            return taxa  # ← RETORNA a taxa lida
        except ValueError:
            print(f'{cores["vermelho"]}{estilos["negrito"]}ERRO: Digite uma taxa válida!{cores["limpa"]}')

def moeda(preço=0):
    """Formata valor como moeda"""
    return f"R$ {preço:.2f}".replace('.', ',')

def aumentar(preço=0, taxa=0, formato=True):
    """Calcula aumento percentual"""
    res = preço + (preço * taxa / 100)
    return moeda(res) if formato else res

def diminuir(preço=0, taxa=0, formato=True):
    """Calcula diminuição percentual"""
    res = preço - (preço * taxa / 100)
    return moeda(res) if formato else res

def dobro(preço=0, formato=True):
    """Calcula o dobro do preço"""
    res = preço * 2
    return moeda(res) if formato else res

def metade(preço=0, formato=True):
    """Calcula a metade do preço"""
    res = preço / 2
    return moeda(res) if formato else res

def resumo(preço, taxa):
    """
    ✅ FUNÇÃO CORRIGIDA - Recebe os valores como parâmetros
    
    Parâmetros:
    - preço: valor já lido e validado
    - taxa: taxa já lida e validada
    """
    print(f"{cores['amarelo']}{estilos['negrito']}{'-' * 30}{cores['limpa']}")
    print(f'{cores["vermelho"]}{estilos["negrito"]}RESUMO DO VALOR{cores["limpa"]}'.center(30))
    print(f"{cores['amarelo']}{estilos['negrito']}{'-' * 30}{cores['limpa']}")
    print(f'{estilos["negrito"]}{cores["cinza"]}Preço analisado: {cores["verde"]}\t{leiaDinheiro(preço, True)}')
    print(f'{estilos["negrito"]}{cores["cinza"]}Dobro do preço: {cores["amarelo"]}\t{dobro(preço, True)}')
    print(f'{estilos["negrito"]}{cores["cinza"]}Metade do preço: {cores["roxo"]}\t{metade(preço, True)}')
    print(f'{estilos["negrito"]}{cores["cinza"]}Com {taxa}% de desconto: {cores["verde"]}\t{diminuir(preço, taxa, True)}')
    print(f'{estilos["negrito"]}{cores["cinza"]}Com {taxa}% de aumento: {cores["vermelho"]}\t{aumentar(preço, taxa, True)}')
    print(f"{cores['amarelo']}{estilos['negrito']}{'-' * 30}{cores['limpa']}")



def leiaDinheiro(msg="Digite um valor: R$ "):
    """Versão mais simples da função"""
    while True:
        try:
            entrada = input(msg).strip()
            
            # Remove símbolos monetários
            valor_limpo = entrada.replace("R$", "").replace("$", "").strip()
            
            # Troca vírgula por ponto
            valor_limpo = valor_limpo.replace(",", ".")
            
            # Converte para float
            valor = float(valor_limpo)
            
            if valor < 0:
                print("❌ ERRO: Valor não pode ser negativo!")
                continue
                
            return valor
            
        except ValueError:
            print(f"❌ ERRO: '{entrada}' é inválido!")

def leiaTaxa(msg="Digite a taxa (%): "):
    while True:
        try:
            entrada = input(msg).strip()
            
            if entrada == "":
                print("❌ ERRO: Digite uma taxa!")
                continue
            
            # Verifica palavras inválidas
            palavras_invalidas = ["MUITO", "POUCO", "ALTO", "BAIXO", "BARATO", "CARO"]
            if any(palavra in entrada.upper() for palavra in palavras_invalidas):
                print(f"❌ ERRO: '{entrada}' não é uma taxa válida!")
                continue
            
            if not any(char.isdigit() for char in entrada):
                print(f"❌ ERRO: '{entrada}' não é uma taxa válida!")
                continue
            
            taxa_limpa = entrada.replace("%", "").replace("+", "").replace(",", ".")
            taxa = float(taxa_limpa)
            
            if taxa < -100:
                print("❌ ERRO: Taxa não pode ser menor que -100%!")
                continue
            
            return taxa
            
        except ValueError:
            print(f"❌ ERRO: '{entrada}' não é uma taxa válida!")
