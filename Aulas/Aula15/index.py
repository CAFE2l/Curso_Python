cont = 1
while cont <= 10:
    print(cont, " -> ", end="")
    cont += 1
print("Acabou")

n = s = 0
while True:
    n = int(input("Digite um número:"))
    if n == 999:
        break
    s += n
# print("A soma vale {}".format(s))
print(f"A soma vale {s}.")

#aprendendo o uso das Fstrings
nome = "Jose"
idade = 33
salario = 986.36
print(f"O {nome}  tem {idade} anos e ganha R${salario:.2f}")

