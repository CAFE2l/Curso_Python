#Minha solução
print("1 para binário")
print("2 para octal")
print("3 para hexadecimal")
escolha = int(input("Escolha uma opção: "))
numero = int(input("Digite um número: "))

if escolha == 1:
    print(bin(numero))
elif escolha == 2:
    print(oct(numero))
elif escolha == 3:
    print(hex(numero))
else:
    print("valor inválido")



#Solução do guaná

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
      [1] converter para BINÁRIO 
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL''')

opção = int(input("Sua opção: "))
if opção == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} converitod para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")