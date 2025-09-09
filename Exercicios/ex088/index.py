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

frase = "🎓📑SISTEMA BOLETIM ESCOLAR📜📝"

print(f"{estilos['negrito']}{cores['amarelo']}{'==='*5}{cores['cinza']}📖📚BOLETIM📐📏{cores['amarelo']}{'==='*4+'=='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['azul']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{'==='*14+'=='}{estilos['reset']}")


# Lista para armazenar todos os alunos
alunos = []

# Coleta de dados dos alunos
while True:
    nome = str(input(f"{cores['cinza']}{estilos['negrito']}Nome: {cores['limpa']}"))
    nota1 = float(input(f"{cores['cinza']}{estilos['negrito']}Nota 1: {cores['limpa']}"))
    nota2 = float(input(f"{cores['cinza']}{estilos['negrito']}Nota 2: {cores['limpa']}"))
    
    # Calcula a média
    media = (nota1 + nota2) / 2
    
    # Adiciona aluno à lista [nome, nota1, nota2, média]
    alunos.append([nome, nota1, nota2, media])
    
    continuar = str(input(f"{cores['cinza']}{estilos['negrito']}Quer continuar? {cores['vermelho']}{estilos['sublinhado']}{estilos['italico']}[S/N]{cores['limpa']} ")).strip().upper()[0]
    if continuar in "Nn":
        break

print(f"{estilos['negrito']}{cores['amarelo']}{"\n" + "=" * 50}{cores['limpa']}")
print(f"{cores['azul']}{estilos['negrito']}{"                 BOLETIM"}")
print(f"{cores['amarelo']}{"=" * 50}{cores['limpa']}")

# Cabeçalho do boletim
print(f"{cores['amarelo']}{estilos['negrito']}{'Nº':<3} {cores['cinza']}{'NOME':<20} {cores['verde']}{'MÉDIA':>8}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{"-" * 35}{cores['limpa']}")

# Exibe boletim com numeração
for indice, aluno in enumerate(alunos):
    nome = aluno[0]
    media = aluno[3]
    print(f"{estilos['negrito']}{cores['amarelo']}{indice:<3} {cores['cinza']}{nome:<20} {cores['verde']}{media:>8.1f}")
print(f"{cores['cinza']}{estilos['negrito']}{"-" * 35}{cores['limpa']}")
print(f"{cores['amarelo']}{"=" * 50}{cores['limpa']}")

# Menu para consultar notas individuais
while True:
    print(f"{"\n"}{cores['ciano']}{estilos['negrito']}Opções:{cores['limpa']}")
    print(f"{estilos['italico']}{estilos['sublinhado']}{cores['vermelho']}999{estilos['reset']} {estilos['negrito']}{cores['vermelho']}- Sair do programa")
    print(f"{estilos['negrito']}{cores['cinza']}Digite o número do aluno para ver suas notas:{cores['limpa']}")
    
    try:
        opcao = int(input(f"{cores['azul']}{estilos['negrito']}Sua escolha:{estilos['reset']} "))
        
        # Opção para sair
        if opcao == 999:
            print(f"{cores['vermelho']}{estilos['sublinhado']}{estilos['italico']}{estilos['negrito']}Finalizando programa...{estilos['reset']}")
            break
        
        # Verifica se o número do aluno existe
        if 0 <= opcao < len(alunos):
            aluno_escolhido = alunos[opcao]
            nome = aluno_escolhido[0]
            nota1 = aluno_escolhido[1]
            nota2 = aluno_escolhido[2]
            media = aluno_escolhido[3]
            
            print(f"\n{cores['cinza']}{estilos['negrito']}Notas de {cores['amarelo']}{nome}:")
            print(f"{cores['cinza']}{estilos['negrito']}Nota 1: {cores['verde']}{nota1:.1f}")
            print(f"{cores['cinza']}{estilos['negrito']}Nota 2: {cores['verde']}{nota2:.1f}")
            print(f"{cores['cinza']}{estilos['negrito']}Média: {cores['amarelo']}{media:.1f}{cores['limpa']}")
            
            # Determina situação do aluno
            if media >= 7.0:
                situacao = f"{estilos['negrito']}{cores['verde']}APROVADO"
            elif media >= 5.0:
                situacao = f"{estilos['negrito']}{cores['amarelo']}RECUPERAÇÃO"
            else:
                situacao = f"{estilos['negrito']}{cores['vermelho']}REPROVADO{cores['limpa']}"
            
            print(f"Situação: {situacao}")
        else:
            print(f"{cores['vermelho']}{estilos['sublinhado']}{estilos['negrito']}{estilos['italico']}ERRO! {estilos['reset']}{cores['vermelho']}{estilos['negrito']}Não existe aluno com número {opcao}{cores['limpa']}")
    
    except ValueError:
        print("ERRO! Digite um número válido!")
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário!")
        break

print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}Programa finalizado!{cores['limpa']}")