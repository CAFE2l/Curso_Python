
#questão 1
numero = int(input("Digite um número: "))
sucessor = numero + 1
antecessor = numero - 1

print("O número digitado foi {}, seu sucessro é {} e seu antecessor é {}".format(numero, sucessor, antecessor))

#questão 2
numero = int(input("Digite um número: "))
print("seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}".format(numero * 2, numero * 3, numero ** (1/2)))

#questão 3
nota1 = float(input("Primeira nota do aluno:"))
nota2 = float(input("Segunda nota do aluno:"))
média = (nota1 + nota2) / 2

print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(nota1, nota2, média))


#questão 4
metros = float(input("Digite uma distância em metros: "))
print ("A mediade de 3.0m correpsonde a: ")
print ("{}km".format(metros / 1000))
print("{}hm".format(metros / 100))
print("{}m".format(metros))
print("{}dm".format(metros * 10))
print("{}cm".format(metros * 100))
print("{}mm".format(metros * 1000))


#questão 5
numero = int(input("Digite um número: "))
print("------------------------------------------------------------")
print("A tabuada do número {} é:".format(numero))
print("{} x 1 = {}".format(numero, numero * 1))
print("{} x 2 = {}".format(numero, numero * 2))
print("{} x 3 = {}".format(numero, numero * 3))
print("{} x 4 = {}".format(numero, numero * 4))
print("{} x 5 = {}".format(numero, numero * 5))
print("{} x 6 = {}".format(numero, numero * 6))
print("{} x 7 = {}".format(numero, numero * 7))
print("{} x 8 = {}".format(numero, numero * 8))
print("{} x 9 = {}".format(numero, numero * 9))
print("{} x 10 = {}".format(numero, numero * 10))
print("------------------------------------------------------------")

#questão 6
carteira = ("Quanto dinheiro você tem na carteira? ")
dinheiro = float(input(carteira))
dólar = dinheiro / 5.60 
print("Com R${:.2f} você pode comprar US${:.2f}".format(dinheiro, dólar))