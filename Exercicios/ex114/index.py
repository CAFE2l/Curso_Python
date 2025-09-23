from modulo.pessoas import cadastrar_pessoa, listar_pessoas


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
frase = "CADASTRO DE PESSOAS FISICAS"

print(f"{estilos['negrito']}{cores['verde']}{"==="*5}{cores['cinza']}CPF{cores['verde']}{"==="*5+"=="}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['verde']}{"==="*11+"=="}{cores['limpa']}") 



def menu():
    while True:
        print(f"{cores['cinza']}{estilos['negrito']}\n1 - Cadastrar pessoa{cores['limpa']}")
        print(f"{cores['cinza']}{estilos['negrito']}2 - Listar pessoas cadastradas{cores['limpa']}")
        print(f"{cores['cinza']}{estilos['negrito']}0 - Sair{cores['limpa']}")
        opcao = input(f"{cores['azul']}{estilos['negrito']}{estilos['italico']}Escolha uma opção: {cores['limpa']}")

        if opcao == "1":
            nome = input(f"{cores['cinza']}{estilos['negrito']}Nome: {estilos['reset']} ")
            idade = input(f"{cores['cinza']}{estilos['negrito']}Idade: {estilos['reset']}")
            if idade.isdigit():
                cadastrar_pessoa(nome, int(idade))
                print(f"{cores['verde']}{estilos['negrito']}Pessoa cadastrada com sucesso!{estilos['reset']}")
            else:
                print(f"{cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']}Idade deve ser um número!{cores['limpa']}")
        elif opcao == "2":
            pessoas = listar_pessoas()
            if pessoas:
                print(f"\nPessoas cadastradas:")
                for pessoa in pessoas:
                    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}")
            else:
                print(f"Nenhuma pessoa cadastrada.")
        elif opcao == "0":
            print(f"{cores['amarelo']}Saindo...{cores['limpa']}")
            break
        else:
            print(f"{cores['vermelho']}{estilos['negrito']}{estilos['sublinhado']}Opção inválida!{cores['limpa']}")