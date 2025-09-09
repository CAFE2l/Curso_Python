# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 4 in num:
#     num.remove(4)
# else:
#     print("Não achei o número 4.")
# print(num)
# print(f"Essa lista tem {len(num)} elementos.")


# valores = []

# for cont in range(0, 5):
#     valores.append(int(input("Digite um valor: ")))

# for c, v in enumerate(valores):
#     print(f"Na posição {c} encontrei o valor {v}!")
# print("Cheguei no final da lista.")


a = [2, 3, 4, 6]
b = a[:] #cópia dos valores de a e não uma ligação entre as listas
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")