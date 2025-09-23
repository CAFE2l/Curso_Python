# 🌐 TESTE DE CONECTIVIDADE - pudim.com.br

print("="*60)
print("🍮 TESTADOR DE SITE - PUDIM.COM.BR")
print("="*60)

# MÉTODO 1: Usando urllib (biblioteca padrão do Python)
print("\n1️⃣ MÉTODO COM urllib (biblioteca padrão):")
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
        print(f"🔍 Testando conexão com {url}...")
        
        # Define timeout de 10 segundos
        response = urllib.request.urlopen(url, timeout=10)
        
        # Verifica o código de resposta
        if response.getcode() == 200:
            print(f"✅ SUCESSO! Site {url} está ACESSÍVEL!")
            print(f"📊 Código de resposta: {response.getcode()}")
            return True
        else:
            print(f"⚠️  Site responde, mas com código: {response.getcode()}")
            return False
            
    except URLError as e:
        print(f"❌ ERRO! Site {url} está INACESSÍVEL!")
        print(f"🚨 Motivo: {e}")
        return False
    except Exception as e:
        print(f"❌ ERRO INESPERADO: {e}")
        return False

# Testando o pudim.com.br
site_pudim = "http://pudim.com.br"
resultado_urllib = testar_site_urllib(site_pudim)

# MÉTODO 2: Usando requests (mais popular, mas precisa instalar)
print("\n" + "="*60)
print("2️⃣ MÉTODO COM requests (mais profissional):")
print("-" * 50)

def testar_site_requests(url):
    """
    Testa site usando requests (precisa instalar: pip install requests)
    """
    try:
        import requests
        
        print(f"🔍 Testando conexão com {url}...")
        
        # Faz a requisição com timeout
        response = requests.get(url, timeout=10)
        
        # Verifica se deu certo
        if response.status_code == 200:
            print(f"✅ SUCESSO! Site {url} está ACESSÍVEL!")
            print(f"📊 Código de resposta: {response.status_code}")
            print(f"⏱️  Tempo de resposta: {response.elapsed.total_seconds():.2f}s")
            return True
        else:
            print(f"⚠️  Site responde, mas com código: {response.status_code}")
            return False
            
    except ImportError:
        print("❌ Biblioteca 'requests' não está instalada!")
        print("💡 Para instalar: pip install requests")
        return False
    except requests.exceptions.Timeout:
        print(f"❌ TIMEOUT! Site {url} demorou muito para responder!")
        return False
    except requests.exceptions.ConnectionError:
        print(f"❌ ERRO DE CONEXÃO! Não conseguiu conectar com {url}!")
        return False
    except Exception as e:
        print(f"❌ ERRO: {e}")
        return False

# Tentando usar requests
try:
    resultado_requests = testar_site_requests(site_pudim)
except:
    print("⚠️  Método requests não disponível, usando apenas urllib")

# MÉTODO 3: Usando socket (mais técnico)
print("\n" + "="*60)
print("3️⃣ MÉTODO COM socket (mais técnico):")
print("-" * 50)

import socket

def testar_site_socket(host, porta=80):
    """
    Testa conectividade usando socket
    
    Parâmetros:
    - host: nome do site (ex: pudim.com.br)
    - porta: porta para testar (padrão: 80 para HTTP)
    """
    try:
        print(f"🔍 Testando conexão socket com {host}:{porta}...")
        
        # Cria socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)  # Timeout de 10 segundos
        
        # Tenta conectar
        resultado = sock.connect_ex((host, porta))
        sock.close()
        
        if resultado == 0:
            print(f"✅ SUCESSO! Porta {porta} de {host} está ABERTA!")
            return True
        else:
            print(f"❌ FALHA! Porta {porta} de {host} está FECHADA!")
            return False
            
    except socket.gaierror:
        print(f"❌ ERRO! Não conseguiu resolver o nome {host}!")
        return False
    except Exception as e:
        print(f"❌ ERRO: {e}")
        return False

# Testando socket
host_pudim = "pudim.com.br"
resultado_socket = testar_site_socket(host_pudim)

# MÉTODO 4: Função completa e profissional
print("\n" + "="*60)
print("4️⃣ FUNÇÃO COMPLETA E PROFISSIONAL:")
print("-" * 50)

def verificar_site_completo(url):
    """
    Função completa para verificar se um site está acessível
    
    Testa várias camadas:
    1. Resolução DNS
    2. Conectividade TCP
    3. Resposta HTTP
    
    Parâmetro:
    - url: URL completa do site
    
    Retorna:
    - dict com informações detalhadas do teste
    """
    import urllib.parse
    
    resultado = {
        'site': url,
        'acessivel': False,
        'tempo_resposta': None,
        'codigo_http': None,
        'erro': None,
        'detalhes': []
    }
    
    try:
        # Parse da URL
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc or parsed.path
        
        resultado['detalhes'].append(f"🔍 Analisando: {url}")
        resultado['detalhes'].append(f"🏠 Host: {host}")
        
        # Teste 1: Resolução DNS
        try:
            import socket
            ip = socket.gethostbyname(host)
            resultado['detalhes'].append(f"✅ DNS OK - IP: {ip}")
        except:
            resultado['erro'] = "Erro na resolução DNS"
            resultado['detalhes'].append("❌ Erro na resolução DNS")
            return resultado
        
        # Teste 2: Conectividade HTTP
        start_time = time.time()
        
        response = urllib.request.urlopen(url, timeout=15)
        
        end_time = time.time()
        resultado['tempo_resposta'] = round(end_time - start_time, 2)
        resultado['codigo_http'] = response.getcode()
        
        if response.getcode() == 200:
            resultado['acessivel'] = True
            resultado['detalhes'].append(f"✅ HTTP OK - Código: {response.getcode()}")
            resultado['detalhes'].append(f"⏱️  Tempo: {resultado['tempo_resposta']}s")
        else:
            resultado['detalhes'].append(f"⚠️  HTTP - Código: {response.getcode()}")
        
    except Exception as e:
        resultado['erro'] = str(e)
        resultado['detalhes'].append(f"❌ Erro: {e}")
    
    return resultado

# Testando função completa
print("\n🧪 TESTE COMPLETO DO PUDIM.COM.BR:")
relatorio = verificar_site_completo("http://pudim.com.br")

print(f"\n📋 RELATÓRIO DETALHADO:")
print(f"🌐 Site: {relatorio['site']}")
print(f"🔗 Acessível: {'✅ SIM' if relatorio['acessivel'] else '❌ NÃO'}")
if relatorio['tempo_resposta']:
    print(f"⏱️  Tempo de resposta: {relatorio['tempo_resposta']}s")
if relatorio['codigo_http']:
    print(f"📊 Código HTTP: {relatorio['codigo_http']}")
if relatorio['erro']:
    print(f"🚨 Erro: {relatorio['erro']}")

print(f"\n📝 Detalhes do teste:")
for detalhe in relatorio['detalhes']:
    print(f"   {detalhe}")

# PROGRAMA PRINCIPAL SIMPLES
print("\n" + "="*60)
print("🎯 PROGRAMA PRINCIPAL SIMPLIFICADO:")
print("-" * 50)

def main():
    """Programa principal para testar o pudim.com.br"""
    
    print("🍮 VERIFICADOR DE SITE - PUDIM.COM.BR")
    print("="*40)
    
    sites_para_testar = [
        "http://pudim.com.br",
        "https://pudim.com.br",
        "http://www.pudim.com.br"
    ]
    
    for site in sites_para_testar:
        print(f"\n🔍 Testando: {site}")
        
        try:
            response = urllib.request.urlopen(site, timeout=10)
            if response.getcode() == 200:
                print(f"✅ {site} está FUNCIONANDO!")
            else:
                print(f"⚠️  {site} - Código: {response.getcode()}")
        except Exception as e:
            print(f"❌ {site} está FORA DO AR!")
            print(f"   Erro: {str(e)[:50]}...")
    
    print("\n" + "="*40)
    print("🎯 TESTE CONCLUÍDO!")

# Executando programa principal
main()

print("\n" + "="*60)
print("📚 EXPLICAÇÃO TÉCNICA:")
print("="*60)

print("""
🎯 O QUE O CÓDIGO FAZ:

1. URLLIB (padrão do Python):
   • Faz requisição HTTP para o site
   • Verifica código de resposta (200 = OK)
   • Não precisa instalar nada

2. REQUESTS (mais popular):
   • Mais fácil de usar
   • Mais informações (tempo, etc.)
   • Precisa: pip install requests

3. SOCKET (baixo nível):
   • Testa conectividade TCP
   • Verifica se porta está aberta
   • Mais técnico

4. FUNÇÃO COMPLETA:
   • Testa DNS, TCP e HTTP
   • Relatório detalhado
   • Informações completas

💡 CÓDIGOS HTTP IMPORTANTES:
• 200 = OK (site funcionando)
• 404 = Não encontrado
• 500 = Erro do servidor
• Timeout = Site muito lento

🎯 PUDIM.COM.BR:
Site clássico brasileiro usado para testes!
Famoso por sua simplicidade e estabilidade.
""")

print("\n🎉 AGORA VOCÊ SABE TESTAR QUALQUER SITE!")
print("="*60)