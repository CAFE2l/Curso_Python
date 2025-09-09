cores = {
    "limpa": "\033[m",
    'vermelho': "\033[31m",
    'verde': "\033[32m",
    'amarelo': "\033[33m",
    'azul': "\033[34m",
    'roxo': "\033[35m",
    'ciano': "\033[36m",
    'cinza': "\033[37m",
    'pretoebranco': '\033[7;30m'
}

fundo = {
    "branco": "\033[40m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m",
    'vermelho_claro': '\033[101m',
    'verde_claro': '\033[102m',
    'amarelo_claro': '\033[103m',
    'azul_claro': '\033[104m',
    'roxo_claro': '\033[105m',
    'ciano_claro': '\033[106m',
    'cinza_claro': '\033[107m'
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
    "duplosublinhado": "\033[21m",  # Sublinhado duplo
    "normal": "\033[22m",           # Desativa negrito e fraco
    "semitalico": "\033[23m",       # Desativa itálico
    "sem_sublinhado": "\033[24m",   # Desativa sublinhado
    "sem_inverso": "\033[27m",      # Desativa inverso
    "visivel": "\033[28m",          # Desativa invisível
    "sem_tachado": "\033[29m"       # Desativa tachado
}




lista = "VALIDADOR DE PARENTÊSES"

print(f"{estilos['negrito']}{cores['azul']}{'==='*5}{cores['cinza']}PARÊNTESES{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['vermelho']}{'==='*5}{estilos['reset']}")
print(f"{cores['cinza']}{estilos['negrito']}{cores['roxo']}{fundo['branco']}{lista.center(39)}{estilos['reset']}")
print(f"{cores['verde']}{estilos['negrito']}{"==="*13+"="}{estilos['reset']}")



def validar_parenteses(expressao):
    """
    Valida se os parênteses estão balanceados em uma expressão.
    Retorna True se estiver correto, False caso contrário.
    """
    pilha = []
    
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) == 0:  # Tentando fechar sem ter aberto
                return False
            pilha.pop()  # Remove o último parêntese aberto
    
    # Se a pilha estiver vazia, todos foram fechados corretamente
    return len(pilha) == 0

def analisar_expressao_detalhada(expressao):
    """
    Análise detalhada mostrando onde está o erro.
    """
    pilha = []
    posicoes_abertas = []
    
    for i, char in enumerate(expressao):
        if char == '(':
            pilha.append(char)
            posicoes_abertas.append(i)
        elif char == ')':
            if len(pilha) == 0:
                return f"Erro na posição {i}: Parêntese fechado sem ter aberto"
            pilha.pop()
            posicoes_abertas.pop()
    
    if len(pilha) > 0:
        return f"Erro: {len(pilha)} parêntese(s) não fechado(s) nas posições: {posicoes_abertas}"
    
    return "Expressão válida!"

# Programa principal

while True:
    expressao = input(f"\n{cores['cinza']}{estilos['negrito']}Digite uma expressão com parênteses {cores['vermelho']}{estilos['sublinhado']}(ou 'sair' para terminar): {estilos['reset']}")
    
    if expressao.lower() == 'sair':
        print(f"{cores['vermelho']}{estilos['negrito']}Programa encerrado!{cores['limpa']}")
        break
    
    # Validação simples
    if validar_parenteses(expressao):
        print(f"{cores['verde']}{estilos['negrito']}✓ VÁLIDA:{cores['cinza']} Os parênteses estão balanceados!{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}{estilos['negrito']}✗ INVÁLIDA:{cores['cinza']} Os parênteses NÃO estão balanceados!{cores['limpa']}")

    # Análise detalhada
    print(f"{cores['cinza']}{estilos['negrito']}Análise detalhada:{cores['limpa']} {cores['verde']}{estilos['negrito']}{analisar_expressao_detalhada(expressao)}{cores['limpa']}")
    
    # Mostrar contadores
    total_abertos = expressao.count('(')
    total_fechados = expressao.count(')')
    print(f"{cores['cinza']}{estilos['negrito']}Parênteses abertos: {cores['verde']}{total_abertos} | {cores['vermelho']}Fechados: {total_fechados}{estilos['reset']}")
    
    print(f"{cores['amarelo']}{estilos['negrito']}=" * 50)