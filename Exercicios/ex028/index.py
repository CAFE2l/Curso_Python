from datetime import date
from time import sleep

ano = int(input("Digite um ano para saber se é bissexto (ou 0 para o ano atual): "))
print("-=-" * 5)
print("PROCESSANDO...")
print("-=-" * 5)
sleep(1.5)

if ano == 0:
    ano = date.today().year  # pega o ano atual se o usuário digitar 0

# Verificação de bissexto:
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

if ano == 0:
    ano = date.today().year


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else: 
    print("O ano {} não é BISSEXTO".format(ano))