cores = {"limpa":"\033[m", 
         'vermelho':"\033[31m",
         'verde':"\033[32m",
         'amarelo':"\033[33m", 
         'azul':"\033[34m", 
         'roxo':"\033[35m",
         'ciano':"\033[36m",
         'cinza':"\033[37m",
         'pretoebranco':'\033[7;30m'}

fundo  = {
         "branco":"\033[m", 
         'vermelho':"\033[41m",
         'verde':"\033[42m",
         'amarelo':"\033[43m", 
         'azul':"\033[44m", 
         'roxo':"\033[45m",
         'ciano':"\033[46m",
         'cinza':"\033[37m"   
}

estilos = {
    "reset": "\033[0m",         # limpa tudo
    "negrito": "\033[1m",
    "fraco": "\033[2m",         # menos intenso
    "italico": "\033[3m",       # nem todo terminal aceita
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",       # troca cor de fundo com a do texto
    "invisivel": "\033[8m",     # oculta o texto (efeito visual)
    "tachado": "\033[9m"        # texto riscado (nem todo terminal mostra)
}

print("-=-"*10)
print(f"{estilos['negrito']}VAMOS ACHAR O LUISSSSSS{estilos['reset']}")
print("-=-"*10)

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)  

if imc < 18.5:
    print(f"{cores['vermelho']}{estilos['negrito']}PAU DE CATAR MANGA{cores['limpa']}, o {cores['vermelho']}{estilos['negrito']}VITOR{cores['limpa']}, planador sem licença KKAKAKAKAK")
elif imc >= 18.5 and imc <= 25:
    print(f"Peso normal -> {cores['azul']}{estilos['negrito']}{estilos['sublinhado']}CAFÉ{cores['limpa']}")
elif imc > 25 and imc <= 30:
    print("João '-' (nada de mais)")
elif imc > 30 and imc <= 40:
    print(f"Aoba, achamos um {cores['amarelo']}{estilos['negrito']}FORDO, gabriel CLT{cores['limpa']}")
else:
    print(f"{cores['vermelho']}{estilos['negrito']}OLOKO LUIS VE SE TIRA A GORDURA DA BUNDA KAKAKAKAKAKAK{cores['limpa']}")


#solução do guaná: 
peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.2f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")
elif  18.5 <= imc < 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE, cuidado")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA, cuidado")