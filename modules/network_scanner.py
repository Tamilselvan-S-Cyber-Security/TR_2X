import socket
import concurrent.futures
from colorama import Fore, Style
from modules.url_validator import extract_domain

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 5900, 8000, 8080, 8443, 8888]

SERVICE_NAMES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    8000: "HTTP-Alt", 8080: "HTTP-Proxy", 8443: "HTTPS-Alt", 8888: "HTTP-Alt"
}

def scan_port(host, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def network_scan(url1, url2=None):
    results = {}
    
    targets = [url1]
    if url2:
        targets.append(url2)
    
    for url in targets:
        domain = extract_domain(url)
        print(f"\n{Fore.CYAN}[*] Scanning: {domain}{Style.RESET_ALL}")
        
        ip = get_ip_address(domain)
        if not ip:
            print(f"{Fore.RED}[!] Could not resolve {domain}{Style.RESET_ALL}")
            results[domain] = {"error": "DNS resolution failed"}
            continue
        
        print(f"{Fore.GREEN}[+] IP Address: {ip}{Style.RESET_ALL}")
        
        open_ports = []
        print(f"{Fore.YELLOW}[*] Scanning common ports...{Style.RESET_ALL}")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            future_to_port = {executor.submit(scan_port, ip, port): port for port in COMMON_PORTS}
            for future in concurrent.futures.as_completed(future_to_port):
                port = future.result()
                if port:
                    open_ports.append(port)
                    service = SERVICE_NAMES.get(port, "Unknown")
                    print(f"{Fore.GREEN}  [+] Port {port}/tcp open - {service}{Style.RESET_ALL}")
        
        if not open_ports:
            print(f"{Fore.YELLOW}[!] No open ports found on common ports{Style.RESET_ALL}")
        
        results[domain] = {
            "ip": ip,
            "open_ports": open_ports,
            "services": {port: SERVICE_NAMES.get(port, "Unknown") for port in open_ports}
        }
    
    return results
