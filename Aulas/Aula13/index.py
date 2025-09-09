#aprendendo a estrutura
# for c in range(6, 0, -1):
#     print(c)
# print("FIM")


#Dando entradas para o usuário
i = int(input("Início: "))
f = int(input("FIM: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
print("FIM")

#Digitando múltiplas vezes
s = 0

for c in range( 0, 3):
    n = int(input("Digite um valor: "))
    s += n 
print("O sumatório de todos os valores foi de: {}" .format(s))
print("FIM")

#
