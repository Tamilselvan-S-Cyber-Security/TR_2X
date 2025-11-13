from colorama import Fore, Style

def display_menu():
    menu = f"""
{Fore.CYAN}
╔═════════════════════════════════════════════════════════════════════════╗
║                      SCANNING OPTIONS                                   ║
╚═════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.GREEN}[1]{Style.RESET_ALL} Network Scanning
    └─ Port detection, service enumeration, host discovery

{Fore.GREEN}[2]{Style.RESET_ALL} Website Bug Bounty
    └─ DNS recon, subdomain enum, SSL validation

{Fore.GREEN}[3]{Style.RESET_ALL} Penetration Testing
    └─ Comprehensive security assessment & vulnerability testing

{Fore.GREEN}[4]{Style.RESET_ALL} DNS Reconnaissance
    └─ DNS records, subdomain discovery, zone transfer

{Fore.GREEN}[5]{Style.RESET_ALL} SSL/TLS Certificate Validation
    └─ Certificate analysis, expiry check, security validation

{Fore.GREEN}[6]{Style.RESET_ALL} Vulnerability Scanning
    └─ XSS, SQLi, LFI, SSRF, Open Redirect, CORS

{Fore.GREEN}[7]{Style.RESET_ALL} Install Required Tools
    └─ Check and install external penetration testing tools

{Fore.RED}[0]{Style.RESET_ALL} Exit TR_2X

{Fore.CYAN}{'═' * 64}{Style.RESET_ALL}
"""
    print(menu)

def get_user_choice():
    while True:
        try:
            choice = input(f"{Fore.YELLOW}[>] Select an option (0-7): {Style.RESET_ALL}").strip()
            choice_int = int(choice)
            if 0 <= choice_int <= 7:
                return choice_int
            else:
                print(f"{Fore.RED}[!] Please enter a number between 0 and 7{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}[!] Invalid input. Please enter a number{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Exiting...{Style.RESET_ALL}")
            exit(0)
