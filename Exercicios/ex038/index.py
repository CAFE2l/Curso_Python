from datetime import datetime, date
#Minha Solução
# Entrada do usuário
nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte a string em data real
nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y").date()

# Data atual
hoje = date.today()

# Cálculo da idade correta (considerando mês e dia)
idade = hoje.year - nascimento.year

# Verifica se ainda não fez aniversário este ano
if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
    idade -= 1

print(f"Você tem {idade} anos.")


if idade < 18:
    print("ainda vai se alistar")
    print(f"faltam {18 - idade} anos")
elif idade == 18:
    print("hora de se alistar")
elif idade > 18:
    print("já passou do tempo do alistamento")
    print(f"já se passaram {idade - 18} anos")



#Solução do Guaná:
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))

if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade 
    print("Ainda faltam {} anos para o alistamento".format(saldo))
    ano = atual + saldo
    print("Seu alistamneto será em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))