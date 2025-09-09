from math import log
valor = float(input("Digite o valor: "))

base = int(input("Digite a base: "))

if base > 0:
    print("base crescente")
L = int(log(valor,base))
print(L)
