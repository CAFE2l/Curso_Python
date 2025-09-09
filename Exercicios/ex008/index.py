produto = "qual o preço do produto?"
preco = float(input("Digite o preço do produto: R$ "))  
desconto = preco * 0.05
preco_final = preco - desconto
print("O produto que custava R$ {:.2f}, com desconto de 5% vai custa R${:.2f}".format(preco, preco_final))
