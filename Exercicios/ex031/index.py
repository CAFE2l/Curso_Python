numero1 = int(input("Digite o valor do primeiro número: "))
numero2  = int(input("Digite o valor do segundos número: "))
numero3 = int(input("Digite o valor do terceiro número: "))


#verificando o menor valor digitado
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

# Verificando quem é maior
maior = numero1 
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3


print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))

