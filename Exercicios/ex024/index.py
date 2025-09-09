from time import sleep
import random

numero = random.randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
tentativa = int(input("Chute um número de 0 a 5: "))

print("PROCESSANDO...")
sleep(1)

if tentativa == numero:
    print("Parabéns! Você acertou.")
else:
    print(f"Você errou. O número era {numero}.")


