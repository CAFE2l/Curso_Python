# nome = input("qual é seu nome? ")
# print(f"Prazer em te Conhecer {nome:=^20}!")


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, o produto é {}, a divisão é {:.2f}, a divisão inteira é {}, e a exponenciação é {}".format(s, m, d, di, e))
# print("A soma vale {}".format(n1+n2-1))