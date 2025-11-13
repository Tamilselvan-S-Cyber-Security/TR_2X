import ssl
import socket
from datetime import datetime
from colorama import Fore, Style
from modules.url_validator import extract_domain

def ssl_certificate_check(url1, url2=None):
    results = {}
    
    targets = [url1]
    if url2:
        targets.append(url2)
    
    for url in targets:
        domain = extract_domain(url)
        print(f"\n{Fore.CYAN}[*] SSL/TLS Certificate Check: {domain}{Style.RESET_ALL}")
        
        cert_info = get_ssl_certificate(domain)
        
        if cert_info:
            results[domain] = cert_info
        else:
            results[domain] = {"error": "Could not retrieve certificate"}
    
    return results

def get_ssl_certificate(domain, port=443):
    try:
        context = ssl.create_default_context()
        
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                
                if not cert:
                    return {"error": "No certificate received"}
                
                subject = dict(x[0] for x in cert.get('subject', []))
                issuer = dict(x[0] for x in cert.get('issuer', []))
                
                subject_cn = subject.get('commonName', 'N/A')
                issuer_org = issuer.get('organizationName', 'N/A')
                
                print(f"{Fore.GREEN}[+] Certificate Subject: {subject_cn}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Certificate Issuer: {issuer_org}{Style.RESET_ALL}")
                
                not_before_str = cert.get('notBefore', '')
                not_after_str = cert.get('notAfter', '')
                
                not_before = datetime.strptime(not_before_str, '%b %d %H:%M:%S %Y %Z')
                not_after = datetime.strptime(not_after_str, '%b %d %H:%M:%S %Y %Z')
                
                days_remaining = (not_after - datetime.now()).days
                
                if days_remaining < 0:
                    print(f"{Fore.RED}[!] Certificate EXPIRED {abs(days_remaining)} days ago{Style.RESET_ALL}")
                elif days_remaining < 30:
                    print(f"{Fore.YELLOW}[!] Certificate expires in {days_remaining} days{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}[+] Certificate valid for {days_remaining} days{Style.RESET_ALL}")
                
                print(f"{Fore.GREEN}[+] Valid From: {not_before.strftime('%Y-%m-%d')}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Valid Until: {not_after.strftime('%Y-%m-%d')}{Style.RESET_ALL}")
                
                san = cert.get('subjectAltName', [])
                if san:
                    san_domains = [x[1] for x in san if x[0] == 'DNS']
                    print(f"{Fore.GREEN}[+] Subject Alternative Names: {len(san_domains)} domains{Style.RESET_ALL}")
                
                version = ssock.version()
                print(f"{Fore.GREEN}[+] TLS Version: {version}{Style.RESET_ALL}")
                
                if version in ['TLSv1', 'TLSv1.1', 'SSLv3', 'SSLv2']:
                    print(f"{Fore.RED}[!] WARNING: Outdated TLS version detected!{Style.RESET_ALL}")
                
                return {
                    "subject": subject_cn,
                    "issuer": issuer_org,
                    "valid_from": not_before.strftime('%Y-%m-%d'),
                    "valid_until": not_after.strftime('%Y-%m-%d'),
                    "days_remaining": days_remaining,
                    "tls_version": version,
                    "san_count": len(san) if san else 0,
                    "status": "expired" if days_remaining < 0 else ("expiring_soon" if days_remaining < 30 else "valid")
                }
    
    except ssl.SSLError as e:
        print(f"{Fore.RED}[!] SSL Error: {str(e)}{Style.RESET_ALL}")
        return {"error": f"SSL Error: {str(e)}"}
    except socket.timeout:
        print(f"{Fore.RED}[!] Connection timeout{Style.RESET_ALL}")
        return {"error": "Connection timeout"}
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
        return {"error": str(e)}
