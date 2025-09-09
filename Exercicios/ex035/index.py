#Minha solução
valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
tempo = int(input("Em quantos anos você vai pagar a casa? "))

parcela = valor / (tempo * 12)
minimo = salario * 30 / 100
print(f"você vai pagar R${parcela:.2f} por mês durante {tempo} anos")

if minimo < parcela:
    print(f"seu empréstimo foi negado devido seu salário de R${salario}")
else:
    print(f"seu empréstimo foi realizado")




#Solução do guaná
casa  = float(input("Valor da casa: R$"))
salário = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))
prestação = casa / (anos * 12)
mínimo = salário * 30 /100
print("Para pagar um casa de R${:.2f} em {} anos".format(casa, anos), end='')
print(" a prestação será de R${:.2f}".format(prestação))
if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")