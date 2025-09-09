# print("\033[0;30;41mTexto com fundo vermelho e letras pretas\033[m")
# print("\033[4;33;46mTexto com fundo ciano e letras amarelas sublinhadas\033[m")
# print("\033[1;35;43mTexto com fundo amarelo e letras roxas\033[m")
# print("\033[0;30;42mTexto com fundo verde e letras brancas \033[m")
# print("\033[mTexto normal padrão\033[m")
# print("\033[7;30mTexto negativo\033[m")



# print("\033[31mOlá, Mundo!")

# a = 3 
# b = 5
# print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!".format(a, b))

nome = "Guanabara"
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

print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format(fundo["vermelho"],nome, cores['limpa']))