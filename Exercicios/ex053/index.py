import datetime

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
#Estilização:
demaior = 'Você é maior de idade???'
print(f"{estilos['negrito']}{cores['roxo']}{"-=" * 28}{estilos['reset']}")
print(f"{estilos['negrito']}{cores['verde']}{fundo['amarelo']}{demaior.center(55)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['roxo']}{"=-" * 28}{estilos['reset']}")


pessoas = 7
anos = []
maior = []
menor = []


today = datetime.date.today()

for i in range(pessoas):
    ano = int(input(f"Digite o ano de nascimento da pessoa {i+1}: "))
    anos.append(ano)
    if today.year - ano >= 18:
        maiores = (f"A pessoa {i+1} é maior de idade.")
        maior.append(maiores)
    else:
        menores = ("A pessoa é não atingiu a maioridade")
        menor.append(menores)

print(f"Os anos digitados foram: {anos}")
print(f"Os maiores de idade foram os {maior} e os menores de idade foram os {menor}")

 

 #Solução do guaná:

atual = datetime.date.today().year
totmaior = 0 
totmenor = 0
for pess in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu? ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E tambem tivemos {} pessoas menores de idade".format(totmenor))
