# arquivo: pessoas.py
def cadastrar_pessoa(nome, idade, arquivo="pessoas.txt", append=True):
    with open(arquivo, "a") as f:
        f.write(f"{nome},{idade}\n")

def listar_pessoas(arquivo="pessoas.txt", append=True):
    pessoas = []
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                nome, idade = linha.strip().split(",")
                pessoas.append((nome, int(idade)))
    except FileNotFoundError:
        pass
    return pessoas
