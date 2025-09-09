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


# print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format(fundo["vermelho"],nome, cores['limpa']))
print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))


    

if r1 == r2 == r3:
    print("os seguimentos acima podem formar um triângulo :D")
    print("Dá para formarmos um {}{}triângulo Equilátero{}".format(cores['vermelho'], estilos['negrito'],cores['limpa']))
    
elif r1 != r2 != r3 != r1:
    print("os seguimentos acima podem formar um triângulo :D")
    print("Dá para formarmos um {}{}triângulo Escaleno{}".format(cores['vermelho'], estilos['negrito'],cores['limpa']))
elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print("os seguimentos acima podem formar um triângulo :D")
    print("Dá para formarmos um {}{}triângulo Isósceles{}".format(cores['vermelho'], estilos['negrito'],cores['limpa']))
else: 
    print("O seguimentos acima não podem formar um triângulo :(")