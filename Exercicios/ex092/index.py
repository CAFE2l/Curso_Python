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

frase = "GOLS DE UM JOGADOR"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5}{cores['cinza']}⚽FUTEBOL⚽{cores['vermelho']}{'==='*4+'=='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{'==='*13}{estilos['reset']}")


# Coleta dados básicos do jogador
nome = str(input(f"{cores['cinza']}{estilos['negrito']}Nome do Jogador: {cores['limpa']}"))
partidas = int(input(f"{cores['cinza']}{estilos['negrito']}Quantas partidas {cores['vermelho']}{nome}{cores['cinza']} jogou? {cores['limpa']}"))

# Lista para armazenar gols de cada partida
gols_por_partida = []

# Coleta gols de cada partida
print(f"\n{estilos['negrito']}{cores['roxo']}---{cores['amarelo']} Registrando gols de {cores['verde']}{nome} {cores['roxo']}---{estilos['negrito']}")
for i in range(partidas):
    gols = int(input(f"{cores['cinza']}{estilos['negrito']}Quantos gols na partida {cores['amarelo']}{estilos['sublinhado']}{estilos['italico']}{i+1}?{cores['limpa']} "))
    gols_por_partida.append(gols)

# Cria o dicionário com todos os dados
jogador = {
    'nome': nome,
    'gols': gols_por_partida,
    'total': sum(gols_por_partida)
}

print(f"{"\n" + "="*50}")
print(f"{"        RELATÓRIO DE APROVEITAMENTO"}")
print(f"{"="*50}")

print(f"{cores['cinza']}{estilos['negrito']}O jogador {cores['amarelo']}{jogador['nome']} {cores['cinza']}jogou {cores['verde']}{len(jogador['gols'])} {cores['cinza']}partidas.")

# Mostra gols por partida
for i, gols in enumerate(jogador['gols']):
    print(f"    {cores['cinza']}{estilos['negrito']}=> Na partida {cores['amarelo']}{i+1}, fez {cores['verde']}{gols}{cores['cinza']} gols.{cores['limpa']}")

print(f"{cores['cinza']}{estilos['negrito']}Total de gols no campeonato: {cores['verde']}{jogador['total']}{estilos['reset']}")

# Estatísticas adicionais
if partidas > 0:
    media = jogador['total'] / partidas
    print(f"{cores['cinza']}{estilos['negrito']}Média de gols por partida: {cores['verde']}{media:.2f}{cores['limpa']}")
    
    if jogador['gols']:  # Se tiver pelo menos uma partida
        melhor_jogo = max(jogador['gols'])
        pior_jogo = min(jogador['gols'])
        print(f"{estilos['negrito']}{cores['cinza']}Melhor partida: {cores['verde']}{melhor_jogo} gols")
        print(f"{estilos['negrito']}{cores['cinza']}Pior partida: {cores['vermelho']}{pior_jogo} gols{cores['limpa']}")

print(f"{cores['azul']}{estilos['negrito']}{"="*50}{cores['limpa']}")
print(f"{cores['verde']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}Dados salvos com sucesso!{estilos['reset']}")

# Exibe o dicionário completo
print(f"\n{cores['cinza']}{estilos['negrito']}Dicionário completo: {cores['vermelho']}{jogador}{estilos['reset']}")