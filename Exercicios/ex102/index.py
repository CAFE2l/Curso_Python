# PROGRAMA FICHA DO JOGADOR
# Função com parâmetros opcionais

def ficha(nome="<desconhecido>", gols=0):
    """
    Mostra a ficha do jogador
    
    Parâmetros opcionais:
    nome: nome do jogador (padrão: "<desconhecido>")
    gols: quantidade de gols (padrão: 0)
    """
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

# Coleta dados do usuário
nome = input("Nome do jogador: ").strip()
gols_input = input("Número de gols: ").strip()

# Processa o nome
if nome == "":
    nome = None  # Usa valor padrão

# Processa os gols
if gols_input == "":
    gols = None  # Usa valor padrão
elif gols_input.isnumeric():
    gols = int(gols_input)
else:
    print("Número inválido! Usando 0.")
    gols = None  # Usa valor padrão

# Chama a função conforme os dados informados
print("\n" + "="*50)
print("RESULTADO:")
print("="*50)

if nome and gols is not None:
    # Tem nome E gols
    ficha(nome, gols)
elif nome:
    # Só tem nome
    ficha(nome)
elif gols is not None:
    # Só tem gols
    ficha(gols=gols)
else:
    # Não tem nada
    ficha()

print("="*50)