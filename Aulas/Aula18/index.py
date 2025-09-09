#Listas dentro de listas

# test = list()
# test.append("gustavo")
# test.append(40)
# galera = list()
# galera.append(test[:])
# test[0] = "maria"
# test[1] = 22
# galera.append(test[:])
# print(galera)


# galera = [["joão", 19], ["ana", 33], ["julia", 22], ["pedro", 15]]
# for p in galera: 
#     print(f"{p[0]} tem {p[1]} anos de idade.")

galera = list()
dado  = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p [1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1
print(f"temos {totmai} maiores e {totmen} menores de idade.")


#