nome = str(input("Digite seu nome: ")).strip()
print("Esse é seu nome com letras maiúsculas: {}".format(nome.upper()))
print("Esse é seu nome com letras minúsculas: {}".format(nome.lower()))
print("Esse é o tanto de caracteres que seu nome tem(sem considerar espaços): {}".format((len(nome.strip())-nome.count(" "))))
first_name = nome.split()
primeiro = first_name[0]
print("Seu primeiro nome tem {} letras".format(len(primeiro)))
