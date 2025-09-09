# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Mostra os 10 primeiros termos
print("\nOs 10 primeiros termos da progressão são:")

for i in range(10):
    termo = primeiro_termo + (i * razao)
    print(termo)

#Solução do Guaná:
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print("{}".format(c), end=(" -> "))
print("Acabou")