def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não digitar esse número.')
            return 0
        else:
            return n