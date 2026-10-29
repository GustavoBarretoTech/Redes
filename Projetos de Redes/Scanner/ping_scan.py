import subprocess

ip_metasploitable = "192.168.56.101"

try:
    ping = subprocess.run(["ping" , "-c", "1", ip_metasploitable],
                          capture_output=True,
                          text=True)
    
    if "1 received" in ping.stdout:
        print("\033[32m-----ALVO VIVO! Iniciando varredura-----\033[0m\n")
        
        nmap = subprocess.run(f"nmap -F -sV {ip_metasploitable}",
                              shell=True,
                              capture_output=True,
                              text=True)
        
        print(nmap.stdout)
    else:
        print("\033[31mAlvo não respondeu ao ping.\033[0m")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
finally:
    print("\nScan Finalizado!")
