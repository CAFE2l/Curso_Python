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
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m"
}
frase = "CONEXÂO COM O PUDIM"

print(f"{estilos['negrito']}{cores['amarelo']}{"==="*5}{cores['cinza']}PUDIM{cores['amarelo']}{"==="*5}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['amarelo']}{"==="*11+"=="}{cores['limpa']}") 


# MÉTODO 1: Usando urllib (biblioteca padrão do Python)
print(f"\n1️⃣ {estilos['negrito']}{cores['cinza']}MÉTODO COM {cores['verde']}urllib {estilos['italico']}(biblioteca padrão):{estilos['reset']}")
print("-" * 50)

import urllib.request
from urllib.error import URLError
import time

def testar_site_urllib(url):
    """
    Testa se um site está acessível usando urllib
    
    Parâmetro:
    - url: endereço do site para testar
    
    Retorna:
    - True se site estiver acessível
    - False se site estiver inacessível
    """
    try:
        # Faz a requisição para o site
        print(f"🔍 {cores['cinza']}{estilos['negrito']}Testando conexão com {url}...{cores['limpa']}")
        
        # Define timeout de 10 segundos
        response = urllib.request.urlopen(url, timeout=10)
        
        # Verifica o código de resposta
        if response.getcode() == 200:
            print(f"✅{cores['verde']}{estilos['negrito']} SUCESSO! Site {url} está ACESSÍVEL!{cores['limpa']}")
            print(f"📊 {cores['cinza']}{estilos['negrito']}{estilos['italico']}Código de resposta: {response.getcode()}{estilos['reset']}")
            return True
        else:
            print(f"⚠️  {cores['amarelo']}{estilos['italico']}{estilos['negrito']}Site responde, mas com código: {response.getcode()}{estilos['reset']}")
            return False
            
    except URLError as e:
        print(f"❌ {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']}ERRO! Site {url} está INACESSÍVEL!{estilos['reset']}")
        print(f"🚨 {cores['vermelho']}{estilos['negrito']}Motivo: {e}{estilos['reset']}")
        return False
    except Exception as e:
        print(f"❌ {cores['vermelho']}{estilos['negrito']}ERRO INESPERADO: {e}{estilos['reset']}")
        return False

# Testando o pudim.com.br
site_pudim = "http://pudim.com.br"
resultado_urllib = testar_site_urllib(site_pudim)

# MÉTODO 2: Usando requests (mais popular, mas precisa instalar)
print(f"{cores['roxo']}{estilos['negrito']}{"\n" + "="*60}{cores['limpa']}")
print(f"2️⃣  {cores['cinza']}{estilos['negrito']}\tMÉTODO COM requests (mais profissional):{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"-" * 50}{cores['limpa']}")

def testar_site_requests(url):
    """
    Testa site usando requests (precisa instalar: pip install requests)
    """
    try:
        import requests
        
        print(f"🔍 {cores['cinza']}{estilos['negrito']}Testando conexão com {url}...{estilos['reset']}")
        
        # Faz a requisição com timeout
        response = requests.get(url, timeout=10)
        
        # Verifica se deu certo
        if response.status_code == 200:
            print(f"✅ {cores['verde']}{estilos['negrito']}SUCESSO! Site {url} está ACESSÍVEL!{estilos['reset']}")
            print(f"📊 {cores['cinza']}{estilos['negrito']}Código de resposta: {response.status_code}{cores['limpa']}")
            print(f"⏱️  {cores['amarelo']}{estilos['negrito']}{estilos['italico']}Tempo de resposta: {response.elapsed.total_seconds():.2f}s{estilos['reset']}{cores['limpa']}")
            return True
        else:
            print(f"⚠️  {cores['amarelo']}{estilos['negrito']}{estilos['italico']}Site responde, mas com código: {response.status_code}{estilos['reset']}")
            return False
            
    except ImportError:
        print(f"❌  {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']}Biblioteca 'requests' não está instalada!{estilos['reset']}")
        print("💡 Para instalar: pip install requests")
        return False
    except requests.exceptions.Timeout:
        print(f"❌  {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']}TIMEOUT! Site {url} demorou muito para responder!{estilos['reset']}")
        return False
    except requests.exceptions.ConnectionError:
        print(f"❌  {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']}ERRO DE CONEXÃO! Não conseguiu conectar com {url}!{estilos['reset']}")
        return False
    except Exception as e:
        print(f"❌  {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']}ERRO: {e}{estilos['reset']}")
        return False

# Tentando usar requests
try:
    resultado_requests = testar_site_requests(site_pudim)
except:
    print("⚠️  Método requests não disponível, usando apenas urllib{estilos['reset']}")

# MÉTODO 3: Usando socket (mais técnico)
print(f"{cores['roxo']}{estilos['negrito']}{"\n" + "="*60}{estilos['reset']}")
print(f"3️⃣ \t{cores['cinza']}{estilos['negrito']}MÉTODO COM socket (mais técnico):{estilos['reset']}")
print(f"{cores['amarelo']}{estilos['negrito']}{"-" * 50}{estilos['reset']}")

import socket

def testar_site_socket(host, porta=80):
    """
    Testa conectividade usando socket
    
    Parâmetros:
    - host: nome do site (ex: pudim.com.br)
    - porta: porta para testar (padrão: 80 para HTTP)
    """
    try:
        print(f"🔍 {cores['cinza']}{estilos['negrito']}Testando conexão socket com {host}:{porta}...{estilos['reset']}")
        
        # Cria socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)  # Timeout de 10 segundos
        
        # Tenta conectar
        resultado = sock.connect_ex((host, porta))
        sock.close()
        
        if resultado == 0:
            print(f"✅ {cores['verde']}{estilos['negrito']}SUCESSO! Porta {porta} de {host} está ABERTA!{estilos['reset']}")
            return True
        else:
            print(f"❌ {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']} FALHA! Porta {porta} de {host} está FECHADA!{estilos['reset']}")
            return False
            
    except socket.gaierror:
        print(f"❌  {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']}ERRO! Não conseguiu resolver o nome {host}!{estilos['reset']}")
        return False
    except Exception as e:
        print(f"❌ {cores['vermelho']}{estilos['italico']}{estilos['negrito']}{estilos['sublinhado']} ERRO: {e}{estilos['reset']}")
        return False

# Testando socket
host_pudim = "pudim.com.br"
resultado_socket = testar_site_socket(host_pudim)


