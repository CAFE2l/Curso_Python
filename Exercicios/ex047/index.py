
#Minha Solução
soma = 0
numeros = []

for i in range(1, 501):          # percorre de 1 até 500 (inclusivo)
    if i % 3 == 0 and i % 2 == 1:  # múltiplo de 3 E ímpar
        soma += i
        numeros.append(i)

print("Números encontrados:", numeros)
print("Quantidade:", len(numeros))
print("Soma:", soma)


#Solução do Guaná:
soma = 0 
cont = 0 
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c       
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))