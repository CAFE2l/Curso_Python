velocidade = float(input("Qua é a velocidade atual do carro? "))

if velocidade > 80:
    print("PARADO AE MALUCO")
    multa = (velocidade - 80) * 7 
    print("MULTADO! Você excedeu o limite de velocidaade permitido que é de 80km/h")
    print(f"Você foi multado em R${multa:.2f}")
else:
    print("Tenha um bom dia! Dirija com segurança!") 