# Lista para armazenar todas as idades
idades = []

# Variáveis para armazenar o homem mais velho
homem_mais_velho = ""
idade_mais_velho = 0
mulher_menos_vinte = ""
for i in range(0, 4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    idades.append(idade)  # guarda a idade para calcular média depois

    # Loop para garantir que o usuário digite apenas 'M' ou 'F'
    while True:
        sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        else:
            print("Opção inválida! Digite apenas M ou F.")

    # Verifica se é homem e se é o mais velho até agora
    if sexo == "M" and idade > idade_mais_velho:
        idade_mais_velho = idade
        homem_mais_velho = nome
    if sexo == "F" and idade < 20:
        mulher_menos_vinte = nome


# Calcula a média
media = sum(idades) / len(idades)

# Resultados
print(f"\nA média das idades é {media:.1f} anos.")

if homem_mais_velho:
    print(f"O homem mais velho foi {homem_mais_velho} com {idade_mais_velho} anos.")
else:
    print("Não foi informado nenhum homem.")


if mulher_menos_vinte:
    print(f"A mulher com menos de 20 anos foi {mulher_menos_vinte}.")
else:
    print("Não foi informada nenhuma mulher com menos de 20 anos.")


#Solução do guaná:

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0 
for p in range(1, 5):
    print("----{} PESSOA ----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))