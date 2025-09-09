nome = str(input("Digite seu nome: "))

print("Seu nome é: {}".format(nome))

primeiro = nome.rsplit()[0]
print("Seu primeiro nome é: {}".format(primeiro))

ultimo = nome.rsplit()[-1]
print("Seu último nome é: {}".format(ultimo))