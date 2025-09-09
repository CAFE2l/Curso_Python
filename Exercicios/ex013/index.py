import math
cateto_oposto = float(input("Digite um valor para o cateto oposto: "))
cateto_adjacente = float(input("Digite um valor para o cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print("A hipotenusa do triângulo é {:.2f}".format(hipotenusa))

co = float(input("comprimento do cateto oposto"))
ca = float(input("comprimento do cateto adjacente"))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {}".format(hi))