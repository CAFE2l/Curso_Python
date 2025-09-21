def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.replace('.', '', 1).isdigit():
            válido = True
            return float(entrada)
        else:
            print(f"{entrada} é um preço inválido!")