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

frase = "CADASTRANDO PESSOAS"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5}{cores['cinza']}CADASTRO{cores['vermelho']}{'==='*5+'='}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['pretoebranco']}{fundo['branco']}{frase.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{'==='*13}{estilos['reset']}")


# LISTAS para armazenar dados de todas as pessoas
pessoas = []  # Lista de dicionários
soma_idades = 0  # Acumulador de idades
mulheres = []  # Lista só com nomes das mulheres

# LOOP para cadastrar várias pessoas
while True:
    print(f"\n{estilos['negrito']}{cores['roxo']}---{cores['cinza']} Cadastrando pessoa {len(pessoas) + 1} {cores['roxo']}---{cores['limpa']}")
    
    nome = str(input(f"{estilos['negrito']}{cores['cinza']}Nome: "))
    
    # Validação do sexo
    while True:
        sexo = str(input(f"{cores['cinza']}{estilos['negrito']}Sexo [M/F]: {estilos['reset']}")).upper().strip()
        if sexo in ['M', 'F']:
            break
        print(f"{cores['vermelho']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}Digite apenas M ou F!{cores['limpa']}")
    
    idade = int(input(f"{cores['cinza']}{estilos['negrito']}Idade: {estilos['reset']}"))
    
    # Criar dicionário da pessoa
    pessoa = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    }
    
    # Adicionar à lista principal
    pessoas.append(pessoa)
    
    # Acumular idade para média
    soma_idades += idade
    
    # Se for mulher, adicionar à lista de mulheres
    if sexo == 'F':
        mulheres.append(nome)
    
    # Pergunta se quer continuar
    continuar = str(input(f"{cores['ciano']}{estilos['negrito']}Quer continuar? {cores['cinza']}{estilos['sublinhado']}{estilos['italico']}[S/N]: ")).upper().strip()
    if continuar == 'N':
        break

print(f"{estilos['negrito']}{cores['amarelo']}{"\n" + "="*50}{cores['limpa']}")
print(f"           {cores['vermelho']}{estilos['negrito']}RELATÓRIO FINAL{cores['limpa']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"="*50}{estilos['reset']}")

# Número total de pessoas
total_pessoas = len(pessoas)
print(f"{estilos['negrito']}{cores['cinza']}O grupo tem {cores['vermelho']}{total_pessoas} {cores['cinza']}pessoas cadastradas.")

# Calcular média de idade
if total_pessoas > 0:
    media_idade = soma_idades / total_pessoas
    print(f"A média de idade do grupo é de {cores['vermelho']}{media_idade:.2f}{cores['cinza']} anos.")
    
    # Mostrar mulheres cadastradas
    if mulheres:
        print(f"As mulheres cadastradas foram: {cores['vermelho']}{', '.join(mulheres)}{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}Nenhuma mulher foi cadastrada.{cores['limpa']}")
    
    # Lista de pessoas acima da média
    print(f"\n{cores['cinza']}{estilos['negrito']}Lista das pessoas que estão acima da média {cores['vermelho']}({media_idade:.2f}{cores['cinza']} anos):")
    pessoas_acima_media = []
    
    for pessoa in pessoas:
        if pessoa['idade'] > media_idade:
            pessoas_acima_media.append(pessoa)
            print(f"  {estilos['negrito']}{cores['vermelho']}-> {cores['azul']}{pessoa['nome']}{cores['cinza']} com {cores['verde']}{pessoa['idade']} {cores['cinza']}anos do sexo {cores['roxo']}{pessoa['sexo']}{cores['limpa']}")
    
    if not pessoas_acima_media:
        print(f"  {estilos['duplosublinhado']}{cores['pretoebranco']}Nenhuma pessoa está acima da média :/{cores['limpa']}")
    
    # Estatísticas extras
    print(f"\n{estilos['negrito']}{cores['roxo']}---{cores['cinza']} ESTATÍSTICAS EXTRAS {cores['roxo']}---{cores['limpa']}")
    homens = [p for p in pessoas if p['sexo'] == 'M']
    print(f"{cores['azul']}{estilos['negrito']}Homens cadastrados: {cores['vermelho']}{len(homens)}{cores['limpa']}")
    print(f"{cores['roxo']}{estilos['negrito']}Mulheres cadastradas:{cores['vermelho']} {len(mulheres)}{cores['limpa']}")
    
    idades = [p['idade'] for p in pessoas]
    print(f"{cores['cinza']}{estilos['negrito']}Pessoa mais nova: {cores['vermelho']}{min(idades)}{cores['cinza']} anos{cores['limpa']}")
    print(f"{cores['cinza']}{estilos['negrito']}Pessoa mais velha: {cores['vermelho']}{max(idades)} {cores['cinza']}anos{cores['limpa']}")
    
else:
    print(f"{cores['vermelho']}{estilos['negrito']}{estilos['sublinhado']}{estilos['italico']}Nenhuma pessoa foi cadastrada.{cores['limpa']}")

print(f"{cores['cinza']}{estilos['negrito']}{cores['amarelo']}{"="*50}{cores['limpa']}")
