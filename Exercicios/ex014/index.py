import math
angulo = int(input("Qual o ângulo que deseja calcular: "))
radianos = math.radians(angulo)

# Cálculos
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print("O número inserido foi {} seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}".format(angulo, seno, cosseno, tangente))


