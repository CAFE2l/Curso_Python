# for c in range(1, 10):
#     print(c)
# print("Fim")


# c = 1 
# while c < 100: 
#     print(c)
#     c += 1
# # print("Fim"
# resposta  = "sim"
# while resposta == "sim":
#     n = int(input("Digite um valor: "))
#     resposta = str(input("Quer continuar? [Sim/Não] ")).lower()
# print("Fim")

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números impares! ".format(par, impar))
print("Acabou")
