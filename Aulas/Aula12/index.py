nome = str(input("Qual é seu nome? "))
#estrutura condicional aninhada
if nome == "Gustavo":
    print("Que nome lindo você tem!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil.")
    #os nomes são separado por espaços
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino")


print("Tenha um bom dia, {}!".format(nome))