cidade = str(input("Digite o nome da sua cidade: ")).strip()

# Converte para minúsculas e verifica se começa com "sant"
if cidade.lower().startswith("sant"):
    print("Sua cidade começa com 'Santo(a)'")
else:
    print("Sua cidade NÃO começa com 'Santo'")
