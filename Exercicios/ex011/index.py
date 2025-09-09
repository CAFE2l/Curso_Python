aluguel = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
preco = (aluguel * 60) + (km * 0.15)
print(f"O total a pagar é de R${preco:.2f}")