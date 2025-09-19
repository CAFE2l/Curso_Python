def notas(*resp):
    resultado = {
        "Total: ": len(resp),
        "Maior: ": max(resp), 
        "Menor: ": min(resp),
        "Média: ": sum(resp) / len(resp)
    }
    return resultado


resp = notas(5.5, 9.5, 10, 6.5)
print(resp)