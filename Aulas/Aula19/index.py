pessoas = {"Nome": "Gustavo", 
           "sexo": "M",
           "idade": 49}
print(pessoas["Nome"])
print(pessoas["sexo"])
print(pessoas["idade"])

print(f"O {pessoas['Nome']} tem {pessoas['idade']} e é do sexo {pessoas['sexo']}")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
# del pessoas['sexo']
pessoas['Nome'] = "Leandro"
pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f"{k} = {v}")

# brasil = []
# estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# estado2 = {"uf": "São Paulo", "sigla": "SP"}

# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)
# print(brasil[0]['uf'])


# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input("Unidade Federativa: "))
#     estado['sigla'] = str(input("Sigla do estado: "))
#     brasil.append(estado) -> faltou a copia do dicionaário
# print(brasil)


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")

