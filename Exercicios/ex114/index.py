import pessoas
from pessoas import cadastrar_pessoa, listar_pessoas

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
                print(f"\n{cores['amarelo']}{estilos['negrito']}{estilos['italico']}Pessoas cadastradas:{cores['limpa']}")
                for pessoa in pessoas:
                    print(f"{cores['vermelho']}{estilos['negrito']}Nome:{cores['cinza']} {pessoa[0]}, {cores['verde']}Idade: {cores['cinza']}{pessoa[1]}{cores['limpa']}")
            else:
                print(f"{cores['vermelho']}{estilos['negrito']}{estilos['italico']}{estilos['sublinhado']}Nenhuma pessoa cadastrada.{cores['limpa']}")
        elif opcao == "0":
            print(f"{cores['amarelo']}{estilos['italico']}{estilos['negrito']}Saindo...{cores['limpa']}")
            break
        else:
            print(f"{cores['vermelho']}{estilos['negrito']}{estilos['sublinhado']}Opção inválida!{cores['limpa']}")


menu()

solution = "SOLUÇÃO DO GUANÁ"

print(f"{estilos['negrito']}{cores['ciano']}{"==="*5}{cores['cinza']}GUANÁ{cores['ciano']}{"==="*5}{cores['limpa']}")
print(f"{cores['pretoebranco']}{estilos['negrito']}{solution.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}{"==="*11+"=="}{cores['limpa']}")

from pessoa import cabeçalho, linha, menu, leiaInt
from time import sleep
from arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrar

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

    criarArquivo = input('Deseja criar o arquivo? [S/N] ').strip().upper()[0]   
    if criarArquivo == 'S':
        try:
            a = open(arq, 'wt+')
            a.close()
        except:
            print('Houve um erro na criação do arquivo!')
        else:
            print(f'Arquivo {arq} criado com sucesso!')
    else:
        print('Saindo do sistema... Até logo!')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)