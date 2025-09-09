# Dicionários de estilos, cores e fundo
cores = {
    "limpa": "\033[m", 
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m", 
    "azul": "\033[34m", 
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
    "pretoebranco": "\033[7;30m"
}

fundo  = {
    "branco": "\033[m", 
    "vermelho": "\033[41m",
    "verde": "\033[42m",
    "amarelo": "\033[43m", 
    "azul": "\033[44m", 
    "roxo": "\033[45m",
    "ciano": "\033[46m",
    "cinza": "\033[47m"   
}

estilos = {
    "reset": "\033[0m", 
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",  
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m"
}

# Cabeçalho do mercado
mercado = "MERCADINHO GOESITANGO"
print(f"{estilos['negrito']}{cores['vermelho']}{'-=-' * 18}{estilos['reset']}")
print(f"{fundo['amarelo']}{estilos['negrito']}{mercado.center(55)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{'-=-' * 18}{estilos['reset']}")

# Catálogo de produtos
produtos = {
    "PAMONHA MELADA REPICADA": 23.59,
    "BACOTA CARAMELIZADA": 10.01,
    "CHAPENUDA RECORTADA": 20.00,
    "XICOTIENO MINUENO": 124.12,
    "PARALEMÃ DOKOTAM": 92.43,
    "OXICATO BEM AMARGO": 120.36,
    "OCOVINHO PEREGRINHO": 920.45
}

print("---" * 20)
print(f"{estilos['negrito']}{'CATÁLOGO'.center(55)}{cores['limpa']}")
for i, (nome, preco) in enumerate(produtos.items(), start=1):
    print(f"{i:02}. {nome:<35} R${preco:>8.2f}")
print("---" * 20)

# Métodos de pagamento
print(f"{estilos['negrito']}{cores['vermelho']}{'-=-' * 18}{estilos['reset']}")
print(f"{estilos['negrito']}{'MÉTODOS DE PAGAMENTO'.center(55)}{cores['limpa']}")

metodos_pagamento = {
    1: ("Dinheiro", -0.10),   # 10% de desconto
    2: ("Boleto", -0.05),     # 5% de desconto
    3: ("Cartão", -0.03),     # 3% de desconto
    4: ("Pix", 0.20),         # 20% de acréscimo
    5: ("Bitcoin", 0.10)     # (brincadeira)
}

for i, (nome, _) in metodos_pagamento.items():
    print(f"{estilos['italico']}{i} - {nome.center(50)}{cores['limpa']}")

# Escolha do pagamento
pagar = int(input("Selecione um método de pagamento: "))

if pagar in metodos_pagamento:
    metodo, valor = metodos_pagamento[pagar]
    print(f"\n{estilos['negrito']}PREÇOS AJUSTADOS ({metodo}){cores['limpa']}")
    print("---" * 20)

    for nome, preco in produtos.items():
        if pagar == 5:
            novo_preco = preco * valor
        else:
            novo_preco = preco + (preco * valor)
        print(f"{nome:<35} R${novo_preco:>8.2f}")
else:
    print("Opção inválida.")

print(f"{estilos['negrito']}{cores['vermelho']}{'-=-' * 18}{estilos['reset']}")
