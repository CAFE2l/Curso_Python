frase = str(input("Digite uma frase qualquer: ")).strip().lower()

quantidade = frase.count('a')
primeira_posicao = frase.find('a') + 1  # +1 porque queremos posição humana (não índice)
ultima_posicao = frase.rfind('a') + 1   # rfind = procura da direita pra esquerda
if "a" in frase:
    print(f"A letra 'A' aparece {quantidade} vezes na frase.")
else:
    print("não houve aparição da letra Aa na frase")
if "a" in frase: 
    print(f"A primeira aparição da letra 'A' é na posição {primeira_posicao}.")
    print(f"A última aparição da letra 'A' é na posição {ultima_posicao}.")
else:
    print("não existe Aa na frase")
