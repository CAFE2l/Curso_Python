from time import sleep

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

help(contador)


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}', end="")

somar(b=4, c=2)

#Programa principal
def test():
    x = 8
    print(f"Na função test, n vale {n}")
    print(f"Na função test, x vale {x}")

n = 2
print(f'Na função n vale {n}')

test()

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')




n1 = 2
funcao()
print(f"N1 fora vale {n1}")

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c 
    return f


# n = int(input("Digite um número: "))
# print(f"O fatorial de {n} é igual a {fatorial(n)}")

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1}, {f2} e {f3}")


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
if par(num):
    print("É par!")
else:
    print("Não é par!")