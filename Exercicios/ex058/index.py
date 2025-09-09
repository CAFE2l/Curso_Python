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
    "branco": "\033[m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m"
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

menu = "Menu de 2 Valores"

# Entrada inicial
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*5 }{cores['amarelo']}{"MENU"}{cores['vermelho']}{"==="*5}{estilos['reset']}")
print(f"{estilos['negrito']}{cores['verde']}{fundo['roxo']}{menu.center(34 )}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['azul']}{"==="*11 + "="}{estilos['reset']}") 



valor1 = int(input(f"Digite o {estilos['negrito']}{cores['amarelo']}primeiro valor:{estilos['reset']} "))
valor2 = int(input(f"Digite o {estilos['negrito']}{cores['amarelo']}primeiro valor:{estilos['reset']} "))

while True:
    print("\nO que você deseja fazer com esses valores:\n")
    menu = [
        f"{estilos['negrito']}[1] Somar{estilos['reset']}",
        f"{estilos['negrito']}[2] Maior{estilos['reset']}",
        f"{estilos['negrito']}[3] Multiplicar{estilos['reset']}",
        f"{estilos['negrito']}[4] Novos números{estilos['reset']}",
        f"{estilos['negrito']}[5] Sair do programa{estilos['reset']}"
    ]

    # Exibindo menu bonito
    for item in menu:
        print(item)

    opcao = int(input("\nDigite sua opção: "))

    if opcao == 1:
        print(f"A soma dos valores {estilos['negrito']}{cores['vermelho']}{valor1}{cores['limpa']} e {estilos['negrito']}{cores['vermelho']}{valor2}{cores['limpa']} é: {cores['vermelho']}{estilos['negrito']}{valor1 + valor2}{cores['limpa']}")
    elif opcao == 2:
        print(f"O maior valor entre {estilos['negrito']}{cores['vermelho']}{valor1}{cores['limpa']} e {estilos['negrito']}{cores['vermelho']}{valor2}{cores['limpa']} é: {cores['vermelho']}{estilos['negrito']}{max(valor1,valor2)}{cores['limpa']}")
    elif opcao == 3:
        print(f"A Multiplicação entre {estilos['negrito']}{cores['vermelho']}{valor1}{cores['limpa']} e {estilos['negrito']}{cores['vermelho']}{valor2}{cores['limpa']} é: {cores['vermelho']}{estilos['negrito']}{valor1 * valor2}{cores['limpa']}")
    elif opcao == 4:
             valor1 = int(input(f"Digite o {estilos['negrito']}{cores['amarelo']}primeiro valor:{estilos['reset']} "))
             valor2 = int(input(f"Digite o {estilos['negrito']}{cores['amarelo']}primeiro valor:{estilos['reset']} "))
    elif opcao == 5:
        print(f"{estilos['negrito']}{cores['amarelo']}Bye Bye 👋{estilos['reset']}")
        break
    else:
        print(f"{cores['vermelho']}Opção inválida!{cores['limpa']}")
