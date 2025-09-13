#TUTORIAL
def título(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
    return
#Programa Principal
# print('-'*30)
# lin()
# print("     CURSO EM VÍDEO    ")
# # print('-'*30)
# lin()
# # print('-'*30)
# lin()
# print("     APRENDA PYTHON    ")
# # print('-'*30)
# lin()
# lin()
# # print('-'*30)
# print("     GUSTAVO GUANABARA    ")
# # print('-'*30)
# lin()

título("   CURSO EM VÍDEO    ")
título('   APRENDA PYTHON    ')
título('   GUSTAVO GUANABARA    ')

#PARTE PRÁTICA
a = 4 
b = 5
s = a + b # ->soma(4,5)  
print(s)
a = 8
b = 9
print(s) # ->soma(8,9)
a = 2
b = 1
s = a + b
print(s) # ->soma(2,1)

def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma {a} + {b} = {s}")

soma(4, 5)
soma(b=8, a=9)
soma(a=2, b=1)
soma(4, 1)

def contador(*num):
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1 

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0 
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")

soma(5, 2)
soma(2, 9, 4)

