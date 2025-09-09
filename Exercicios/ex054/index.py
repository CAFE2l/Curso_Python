
peso = []
for i in range (0, 5):
    p = float(input("Digite seu peso? "))
    peso.append(p)

maior = max(peso)
menor = min(peso)


print(f"o maior peso foi {maior}, e o menor peso foi {menor}")


#Solução do Guaná:
maior = 0
menor = 0 
for p in range(1, 6):
    peso = float(input("Peso da {} pessoa: ".format(p))) 
    if p == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("O maior peso lido foi de {}Kg".format(maior))
print("O menor peso lido foi de {}Kg".format(menor))