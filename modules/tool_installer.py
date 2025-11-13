import subprocess
import shutil
from colorama import Fore, Style

EXTERNAL_TOOLS = {
    'subfinder': {
        'description': 'Fast subdomain discovery tool',
        'install': 'go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest',
        'check': 'subfinder'
    },
    'nuclei': {
        'description': 'Vulnerability scanner based on templates',
        'install': 'go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest',
        'check': 'nuclei'
    },
    'httpx': {
        'description': 'Fast HTTP toolkit',
        'install': 'go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest',
        'check': 'httpx'
    },
    'amass': {
        'description': 'In-depth attack surface mapping',
        'install': 'go install -v github.com/OWASP/Amass/v3/...@master',
        'check': 'amass'
    },
    'gau': {
        'description': 'Get All URLs from various sources',
        'install': 'go install github.com/lc/gau/v2/cmd/gau@latest',
        'check': 'gau'
    },
    'nmap': {
        'description': 'Network scanner',
        'install': 'System package: sudo apt install nmap (Debian/Ubuntu) or sudo yum install nmap (RHEL/CentOS)',
        'check': 'nmap'
    },
    'wpscan': {
        'description': 'WordPress vulnerability scanner',
        'install': 'System package: sudo apt install wpscan or gem install wpscan',
        'check': 'wpscan'
    }
}

def check_and_install_tools():
    print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║            EXTERNAL TOOLS INSTALLATION GUIDE             ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    print(f"{Fore.YELLOW}[*] Checking for external penetration testing tools...{Style.RESET_ALL}\n")
    
    installed = []
    not_installed = []
    
    for tool_name, tool_info in EXTERNAL_TOOLS.items():
        if shutil.which(tool_info['check']):
            installed.append(tool_name)
            print(f"{Fore.GREEN}[✓] {tool_name:<15} - Installed{Style.RESET_ALL}")
        else:
            not_installed.append(tool_name)
            print(f"{Fore.RED}[✗] {tool_name:<15} - Not Found{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'═' * 64}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Installed: {len(installed)}/{len(EXTERNAL_TOOLS)}{Style.RESET_ALL}")
    
    if not_installed:
        print(f"\n{Fore.YELLOW}[!] Installation Instructions for Missing Tools:{Style.RESET_ALL}\n")
        
        for tool_name in not_installed:
            tool_info = EXTERNAL_TOOLS[tool_name]
            print(f"{Fore.CYAN}▶ {tool_name}{Style.RESET_ALL}")
            print(f"  Description: {tool_info['description']}")
            print(f"  Install: {tool_info['install']}\n")
        
        print(f"{Fore.YELLOW}[*] Note: TR_2X works without external tools but provides basic scanning.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Install external tools for advanced features and comprehensive scans.{Style.RESET_ALL}\n")
    else:
        print(f"\n{Fore.GREEN}[+] All external tools are installed!{Style.RESET_ALL}\n")
    
    return {
        'installed': installed,
        'not_installed': not_installed,
        'total': len(EXTERNAL_TOOLS)
    }
