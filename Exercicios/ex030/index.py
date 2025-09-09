# print("Digite o comprimento de três retas:")
# a = float(input("Primeira reta: "))
# b = float(input("Segunda reta: "))
# c = float(input("Terceira reta: "))

# # Regra: uma reta só forma triângulo se for menor que a soma das outras duas
# if a < b + c and b < a + c and c < a + b:
#     print("✅ As retas podem formar um triângulo!")
# else:
#     print("❌ As retas NÃO podem formar um triângulo.")


print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os seguimentos acima podem formar um triângulo :D")
else: 
    print("O seguimentos acima não podem formar um triângulo :(")