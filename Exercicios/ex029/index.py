salário = float(input("Digite seu salário: "))
if salário >= 1250:
    aumento = salário * 0.1
    print("Seu salário aumentou de {}, para {}".format(salário, aumento + salário))
else: 
    aumento = salário * 0.15
    print("Seu salário aumentou de {}, para {}".format(salário, aumento + salário))