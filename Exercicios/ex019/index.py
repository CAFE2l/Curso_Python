numero = int(input("Digite um número de 0 a 9999: "))

if 0 <= numero <= 9999:
    unidade = numero % 10
    dezena = (numero // 10) % 10 
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10 

    print(f"Unidade = {unidade}")
    print(f"Dezena = {dezena}")
    print(f"Centena = {centena}")
    print(f"Milhar = {milhar}")
else:
    print("Número fora do intervalo! Digite de 0 a 9999.")
