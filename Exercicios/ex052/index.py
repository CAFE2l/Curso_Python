# Ler a frase do usuário
frase = input("Digite uma frase: ")

# Remover espaços e deixar tudo minúsculo
frase_sem_espacos = ""
for letra in frase:
    if letra != " ":
        frase_sem_espacos += letra.lower()

# Inverter a frase usando for loop
frase_invertida = ""
for i in range(len(frase_sem_espacos) - 1, -1, -1):
    frase_invertida += frase_sem_espacos[i]

# Verificar se é palíndromo
if frase_sem_espacos == frase_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")


#Solução do guaná 

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
inverso = junto[::-1]
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto: 
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palídromo!")
