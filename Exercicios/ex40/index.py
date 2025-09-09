from datetime import datetime, date

# Entrada do usuário
nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte a string em data real
nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()

# Data atual
hoje = date.today()

# Cálculo da idade correta (considerando mês e dia)
idade = hoje.year - nascimento.year



if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 25:
    print("SENIOR")
else:
    print("MASTER")


#Solução do Guaná:
atual = date.today().year
nascimento = int(input("Ano de Nascimento: "))
idade = atual - nascimento
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SENIOR")
else:
    print("Classificação: MASTER")