nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
média = (nota1 + nota2) / 2
print("A sua média foi {:.2f}".format(média))
print("PARABÉNS" if média >= 7.5 else "VAI TRABALHAR VAGABUNDO")

if média >= 6:
    print("Sua média foi boa")
else: 
    print("Sua média foi ruim! ESTUDE MAIS!!!!!!!!!!")