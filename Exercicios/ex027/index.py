from time import sleep

viagem = float(input("Quantos Km vc rodou? "))
print("Você está prestes a começar uma viagem de {}Km".format(viagem))
print("-=-" * 10)
print("PROCESSANDO...")
print("-=-" * 10)
sleep(2) # Pausa o programa por 1 segundo

preço  = viagem * 0.50 if viagem <= 200 else viagem * 0.45

if viagem <= 200:
    print("para viagens até 200km vc paga R$0,50 por km")
    preço = viagem * 0.50
    print("sua viagem ficou R${:.2f}".format(preço))
else:
     preço = viagem * 0.45
     print("sua viagem ficou R${:.2f}".format(preço))