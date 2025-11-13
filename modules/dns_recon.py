import socket
import subprocess
from colorama import Fore, Style
from modules.url_validator import extract_domain

def dns_reconnaissance(url1, url2=None):
    results = {}
    
    targets = [url1]
    if url2:
        targets.append(url2)
    
    for url in targets:
        domain = extract_domain(url)
        print(f"\n{Fore.CYAN}[*] DNS Reconnaissance: {domain}{Style.RESET_ALL}")
        
        domain_info = {}
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"{Fore.GREEN}[+] A Record: {ip}{Style.RESET_ALL}")
            domain_info['A'] = ip
        except:
            print(f"{Fore.RED}[!] Could not resolve A record{Style.RESET_ALL}")
            domain_info['A'] = None
        
        try:
            hostname = socket.gethostbyaddr(domain_info.get('A', domain))[0]
            print(f"{Fore.GREEN}[+] PTR Record: {hostname}{Style.RESET_ALL}")
            domain_info['PTR'] = hostname
        except:
            domain_info['PTR'] = None
        
        record_types = ['NS', 'MX', 'TXT', 'CNAME', 'SOA']
        for record_type in record_types:
            try:
                result = subprocess.run(
                    ['nslookup', '-type=' + record_type, domain],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0 and record_type.lower() in result.stdout.lower():
                    print(f"{Fore.GREEN}[+] {record_type} Record found{Style.RESET_ALL}")
                    domain_info[record_type] = result.stdout
            except:
                pass
        
        subdomains = check_common_subdomains(domain)
        if subdomains:
            print(f"{Fore.GREEN}[+] Found {len(subdomains)} common subdomains{Style.RESET_ALL}")
            for subdomain in subdomains:
                print(f"{Fore.CYAN}  └─ {subdomain}{Style.RESET_ALL}")
            domain_info['subdomains'] = subdomains
        
        results[domain] = domain_info
    
    return results

def check_common_subdomains(domain):
    common_subs = ['www', 'mail', 'ftp', 'admin', 'blog', 'dev', 'api', 'staging', 'test', 'portal']
    found_subdomains = []
    
    print(f"{Fore.YELLOW}[*] Checking common subdomains...{Style.RESET_ALL}")
    
    for sub in common_subs:
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            found_subdomains.append(subdomain)
        except:
            pass
    
    return found_subdomains
