cores = {"limpa":"\033[m", 
         'vermelho':"\033[31m",
         'verde':"\033[32m",
         'amarelo':"\033[33m", 
         'azul':"\033[34m", 
         'roxo':"\033[35m",
         'ciano':"\033[36m",
         'cinza':"\033[37m",
         'pretoebranco':'\033[7;30m'}

fundo  = {
         "branco":"\033[m", 
         'vermelho':"\033[41m",
         'verde':"\033[42m",
         'amarelo':"\033[43m", 
         'azul':"\033[44m", 
         'roxo':"\033[45m",
         'ciano':"\033[46m",
         'cinza':"\033[37m"   
}




#Minha Solução
print("{}-=-{}{}".format(fundo["amarelo"], cores['vermelho'],cores['limpa'])* 10)
print("REPROVADO OU APROVADO (boravê)")
print("{}-=-{}{}".format(fundo["amarelo"], cores['vermelho'],cores['limpa'])* 10)
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2
print(f"sua média foi de {media}")
if media < 5:
    print("REPROVADO")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO")
elif media >= 7:
    print("APROVADO")
else: 
    print("VAI ESTUDAR VAGABUNDO")



#Solução do Guaná:
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
média = (nota1 + nota2) / 2
print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, média))


if média >= 5 and média < 7:
    print("O aluno está em RECUPERAÇÃO.")
elif média < 5:
    print("O aluno está REPROVADO.")
elif média >= 7:
    print("O aluno está APROVADO.")
else:
    print("VAI ESTUDAR VAGABUNDO")