# SISTEMA DE GESTÃO DE JOGADORES DE FUTEBOL
# Versão aprimorada com múltiplos jogadores e sistema de visualização

# Dicionários para cores e estilos (igual ao original)
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

# LISTA PRINCIPAL que vai armazenar TODOS os jogadores
# Cada elemento da lista será um dicionário com os dados de um jogador
time = []

def exibir_cabecalho():
    """Função para exibir o cabeçalho do programa"""
    print(f"{estilos['negrito']}{cores['azul']}{'==='*5}{cores['cinza']}⚽FUTEBOL⚽{cores['vermelho']}{'==='*4+'=='}{estilos['reset']}")
    print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{'SISTEMA DE GESTÃO DE JOGADORES'.center(39)}{estilos['reset']}")
    print(f"{cores['verde']}{estilos['negrito']}{'==='*13}{estilos['reset']}")

def cadastrar_jogador():
    """Função para cadastrar um novo jogador"""
    print(f"\n{estilos['negrito']}{cores['roxo']}--- CADASTRO DE NOVO JOGADOR ---{estilos['reset']}")
    
    # Coleta dados básicos
    nome = str(input(f"{cores['cinza']}{estilos['negrito']}Nome do Jogador: {cores['limpa']}"))
    partidas = int(input(f"{cores['cinza']}{estilos['negrito']}Quantas partidas {cores['vermelho']}{nome}{cores['cinza']} jogou? {cores['limpa']}"))
    
    # Lista para os gols deste jogador específico
    gols_por_partida = []
    
    # Coleta gols de cada partida
    print(f"\n{estilos['negrito']}{cores['roxo']}--- Registrando gols de {cores['verde']}{nome} {cores['roxo']}---{estilos['reset']}")
    for i in range(partidas):
        gols = int(input(f"{cores['cinza']}{estilos['negrito']}Quantos gols na partida {cores['amarelo']}{estilos['sublinhado']}{estilos['italico']}{i+1}?{cores['limpa']} "))
        gols_por_partida.append(gols)
    
    # Cria o dicionário do jogador
    jogador = {
        'nome': nome,
        'gols': gols_por_partida,
        'total': sum(gols_por_partida),
        'partidas': partidas
    }
    
    # ADICIONA o jogador na lista principal do time
    time.append(jogador)
    
    print(f"{cores['verde']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}Jogador {nome} cadastrado com sucesso!{estilos['reset']}")

def listar_jogadores():
    """Função para mostrar todos os jogadores cadastrados"""
    if not time:  # Se a lista estiver vazia
        print(f"{cores['vermelho']}{estilos['negrito']}Nenhum jogador cadastrado ainda!{estilos['reset']}")
        return
    
    print(f"\n{cores['azul']}{estilos['negrito']}{'='*50}")
    print(f"{'LISTA DE JOGADORES CADASTRADOS'.center(50)}")
    print(f"{'='*50}{estilos['reset']}")
    
    for i, jogador in enumerate(time):
        print(f"{cores['amarelo']}{estilos['negrito']}{i+1}. {jogador['nome']} - {cores['verde']}{jogador['total']} gols em {jogador['partidas']} partidas{estilos['reset']}")

def exibir_detalhes_jogador(jogador):
    """Função para exibir detalhes completos de um jogador"""
    print(f"\n{cores['azul']}{estilos['negrito']}{'='*50}")
    print(f"{'RELATÓRIO DETALHADO'.center(50)}")
    print(f"{'='*50}{estilos['reset']}")
    
    print(f"{cores['cinza']}{estilos['negrito']}Jogador: {cores['amarelo']}{jogador['nome']}")
    print(f"{cores['cinza']}{estilos['negrito']}Partidas jogadas: {cores['verde']}{jogador['partidas']}")
    print(f"{cores['cinza']}{estilos['negrito']}Total de gols: {cores['verde']}{jogador['total']}{estilos['reset']}")
    
    # Detalhes por partida
    print(f"\n{cores['roxo']}{estilos['negrito']}--- GOLS POR PARTIDA ---{estilos['reset']}")
    for i, gols in enumerate(jogador['gols']):
        print(f"    {cores['cinza']}{estilos['negrito']}=> Partida {cores['amarelo']}{i+1}: {cores['verde']}{gols} gols{cores['limpa']}")
    
    # Estatísticas calculadas
    if jogador['partidas'] > 0:
        media = jogador['total'] / jogador['partidas']
        print(f"\n{cores['roxo']}{estilos['negrito']}--- ESTATÍSTICAS ---{estilos['reset']}")
        print(f"{cores['cinza']}{estilos['negrito']}Média de gols por partida: {cores['verde']}{media:.2f}")
        
        if jogador['gols']:
            melhor_jogo = max(jogador['gols'])
            pior_jogo = min(jogador['gols'])
            print(f"{cores['cinza']}{estilos['negrito']}Melhor partida: {cores['verde']}{melhor_jogo} gols")
            print(f"{cores['cinza']}{estilos['negrito']}Pior partida: {cores['vermelho']}{pior_jogo} gols")
            
            # Quantas partidas sem gols
            jogos_sem_gols = jogador['gols'].count(0)
            print(f"{cores['cinza']}{estilos['negrito']}Jogos sem marcar: {cores['vermelho']}{jogos_sem_gols}")
            
            # Quantas partidas com mais de 1 gol
            jogos_multiplos_gols = len([g for g in jogador['gols'] if g > 1])
            print(f"{cores['cinza']}{estilos['negrito']}Jogos com múltiplos gols: {cores['verde']}{jogos_multiplos_gols}{estilos['reset']}")

def ver_detalhes_por_escolha():
    """Função para o usuário escolher qual jogador ver detalhes"""
    if not time:
        print(f"{cores['vermelho']}{estilos['negrito']}Nenhum jogador cadastrado ainda!{estilos['reset']}")
        return
    
    listar_jogadores()
    
    try:
        escolha = int(input(f"\n{cores['cinza']}{estilos['negrito']}Digite o número do jogador para ver detalhes: {cores['limpa']}"))
        if 1 <= escolha <= len(time):
            jogador_escolhido = time[escolha - 1]  # -1 porque lista começa em 0
            exibir_detalhes_jogador(jogador_escolhido)
        else:
            print(f"{cores['vermelho']}{estilos['negrito']}Número inválido!{estilos['reset']}")
    except ValueError:
        print(f"{cores['vermelho']}{estilos['negrito']}Por favor, digite um número válido!{estilos['reset']}")

def estatisticas_do_time():
    """Função para mostrar estatísticas gerais do time"""
    if not time:
        print(f"{cores['vermelho']}{estilos['negrito']}Nenhum jogador cadastrado ainda!{estilos['reset']}")
        return
    
    print(f"\n{cores['azul']}{estilos['negrito']}{'='*50}")
    print(f"{'ESTATÍSTICAS GERAIS DO TIME'.center(50)}")
    print(f"{'='*50}{estilos['reset']}")
    
    # Calcula estatísticas gerais
    total_gols_time = sum(jogador['total'] for jogador in time)
    total_partidas_time = sum(jogador['partidas'] for jogador in time)
    
    print(f"{cores['cinza']}{estilos['negrito']}Total de jogadores: {cores['verde']}{len(time)}")
    print(f"{cores['cinza']}{estilos['negrito']}Total de gols do time: {cores['verde']}{total_gols_time}")
    print(f"{cores['cinza']}{estilos['negrito']}Total de partidas: {cores['verde']}{total_partidas_time}")
    
    if total_partidas_time > 0:
        media_time = total_gols_time / total_partidas_time
        print(f"{cores['cinza']}{estilos['negrito']}Média de gols por partida (time): {cores['verde']}{media_time:.2f}")
    
    # Jogador com mais gols
    artilheiro = max(time, key=lambda j: j['total'])
    print(f"{cores['cinza']}{estilos['negrito']}Artilheiro do time: {cores['amarelo']}{artilheiro['nome']} {cores['cinza']}com {cores['verde']}{artilheiro['total']} gols")
    
    # Jogador com melhor média
    jogador_melhor_media = max(time, key=lambda j: j['total'] / j['partidas'] if j['partidas'] > 0 else 0)
    melhor_media = jogador_melhor_media['total'] / jogador_melhor_media['partidas'] if jogador_melhor_media['partidas'] > 0 else 0
    print(f"{cores['cinza']}{estilos['negrito']}Melhor média: {cores['amarelo']}{jogador_melhor_media['nome']} {cores['cinza']}com {cores['verde']}{melhor_media:.2f} gols/jogo{estilos['reset']}")

def menu():
    """Função que exibe o menu principal"""
    while True:
        print(f"\n{cores['azul']}{estilos['negrito']}{'='*30}")
        print(f"{'MENU PRINCIPAL'.center(30)}")
        print(f"{'='*30}{estilos['reset']}")
        print(f"{cores['verde']}{estilos['negrito']}1 - Cadastrar novo jogador")
        print(f"2 - Listar todos os jogadores") 
        print(f"3 - Ver detalhes de um jogador")
        print(f"4 - Estatísticas do time")
        print(f"5 - Sair{estilos['reset']}")
        
        try:
            opcao = int(input(f"\n{cores['cinza']}{estilos['negrito']}Digite sua opção: {cores['limpa']}"))
            
            if opcao == 1:
                cadastrar_jogador()
            elif opcao == 2:
                listar_jogadores()
            elif opcao == 3:
                ver_detalhes_por_escolha()
            elif opcao == 4:
                estatisticas_do_time()
            elif opcao == 5:
                print(f"{cores['verde']}{estilos['negrito']}Obrigado por usar o sistema!{estilos['reset']}")
                break
            else:
                print(f"{cores['vermelho']}{estilos['negrito']}Opção inválida! Tente novamente.{estilos['reset']}")
                
        except ValueError:
            print(f"{cores['vermelho']}{estilos['negrito']}Por favor, digite um número válido!{estilos['reset']}")

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    exibir_cabecalho()
    menu()