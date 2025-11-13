from colorama import Fore, Style

def display_banner():
    banner = f"""{Fore.CYAN}
╔═════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                     ║
║  ████████╗██████╗     ██████╗ ██╗  ██╗                                              ║
║  ╚══██╔══╝██╔══██╗    ╚════██╗╚██╗██╔╝                                              ║
║     ██║   ██████╔╝     █████╔╝ ╚███╔╝                                               ║
║     ██║   ██╔══██╗    ██╔═══╝  ██╔██╗                                               ║
║     ██║   ██║  ██║    ███████╗██╔╝ ██╗                                              ║
║     ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝                                              ║
║                                                                                     ║
║                    {Fore.YELLOW}Threat Recon 2X{Fore.CYAN}                          ║
║        Advanced Penetration Testing & Bug Bounty Tool                               ║
║                                                                                     ║
║              {Fore.GREEN}Developed by CyberWolf Team{Fore.CYAN}                     ║
║        {Fore.WHITE}https://github.com/Tamilselvan-S-Cyber-Security/TR_2X{Fore.CYAN} ║
║                                                                                     ║
║  {Fore.YELLOW}[*] Network Scanning & Reconnaissance{Fore.CYAN}                      ║
║  {Fore.YELLOW}[*] Vulnerability Detection & Analysis{Fore.CYAN}                     ║
║  {Fore.YELLOW}[*] DNS Enumeration & SSL Validation{Fore.CYAN}                       ║
║  {Fore.YELLOW}[*] Automated Bug Bounty Workflows{Fore.CYAN}                         ║
║                                                                                     ║
╚═════════════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""
    print(banner)
