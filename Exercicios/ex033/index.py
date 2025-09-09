a = int(input("valor de a "))
b = int(input("valor de b "))
c = int(input("Valor de c "))
if a == 0:
  print("Não é uma equação de segundo grau")
  a = 1
else:
    delta = (b**2) - (4*a*c)
    print(delta)
    raiz_quadrada = delta**(1/2)
    print(raiz_quadrada)
x1 = (-b + raiz_quadrada) / (2*a)
x2 = (-b - raiz_quadrada) / (2*a)
print("As raízes da equação são", x1, "e", x2)
Vx = (-b) / (2*a)
Vy = (- delta) / (4*a)
print("O vértice da parábola está no ponto:", (Vx, Vy))
if a < 0:
  print("concavidade vira pra baixo")
else:
  print("concavidade vira pra cima")
if c > 0:
  print(f" da parábola inicia-se no ponto {c} do eixo y")
else:
  print(f" da parábola inicia-se no ponto {c} do eixo y")




