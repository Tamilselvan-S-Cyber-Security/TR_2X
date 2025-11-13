#!/usr/bin/env python3

import sys
import os
import argparse
from colorama import init, Fore, Style
from modules.banner import display_banner
from modules.menu import display_menu, get_user_choice
from modules.network_scanner import network_scan
from modules.dns_recon import dns_reconnaissance
from modules.ssl_validator import ssl_certificate_check
from modules.vulnerability_scanner import vulnerability_scan
from modules.tool_installer import check_and_install_tools
from modules.result_exporter import export_results
from modules.url_validator import validate_url

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(
        description='TR_2X (Threat Recon 2X) - Advanced Penetration Testing CLI Tool by CyberWolf Team',
        epilog='Developed by CyberWolf Team | https://github.com/Tamilselvan-S-Cyber-Security/TR_2X'
    )
    parser.add_argument('-u', '--url', help='Primary target URL', type=str)
    parser.add_argument('-u2', '--url2', help='Secondary target URL (optional)', type=str)
    parser.add_argument('-m', '--mode', help='Scanning mode (1-7)', type=int, choices=[1, 2, 3, 4, 5, 6, 7])
    parser.add_argument('-o', '--output', help='Output file path', type=str)
    parser.add_argument('--install', help='Check and install required tools', action='store_true')
    
    args = parser.parse_args()
    
    display_banner()
    
    if args.install:
        check_and_install_tools()
        return
    
    if args.mode == 7:
        check_and_install_tools()
        return
    
    if args.url:
        url1 = validate_url(args.url)
        url2 = validate_url(args.url2) if args.url2 else None
        
        if args.mode:
            run_scan(args.mode, url1, url2, args.output)
        else:
            interactive_mode(url1, url2)
    else:
        interactive_mode()

def interactive_mode(url1=None, url2=None):
    if not url1:
        print(f"{Fore.CYAN}[+] Enter target URL 1: {Style.RESET_ALL}", end='')
        url1_input = input().strip()
        url1 = validate_url(url1_input)
        
        print(f"{Fore.CYAN}[+] Enter target URL 2 (optional, press Enter to skip): {Style.RESET_ALL}", end='')
        url2_input = input().strip()
        url2 = validate_url(url2_input) if url2_input else None
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 0:
            print(f"\n{Fore.GREEN}[+] Thank you for using TR_2X! Stay safe, CyberWolf Team{Style.RESET_ALL}")
            sys.exit(0)
        elif choice == 7:
            check_and_install_tools()
        else:
            run_scan(choice, url1, url2)

def run_scan(mode, url1, url2=None, output_file=None):
    results = {}
    
    try:
        if mode == 1:
            print(f"\n{Fore.YELLOW}[*] Starting Network Scanning...{Style.RESET_ALL}")
            results['network_scan'] = network_scan(url1, url2)
        
        elif mode == 2:
            print(f"\n{Fore.YELLOW}[*] Starting Bug Bounty Reconnaissance...{Style.RESET_ALL}")
            results['bug_bounty'] = {
                'dns_recon': dns_reconnaissance(url1, url2),
                'ssl_check': ssl_certificate_check(url1, url2)
            }
        
        elif mode == 3:
            print(f"\n{Fore.YELLOW}[*] Starting Penetration Testing...{Style.RESET_ALL}")
            results['pentest'] = {
                'network': network_scan(url1, url2),
                'vulnerabilities': vulnerability_scan(url1, url2)
            }
        
        elif mode == 4:
            print(f"\n{Fore.YELLOW}[*] Starting DNS Reconnaissance...{Style.RESET_ALL}")
            results['dns_recon'] = dns_reconnaissance(url1, url2)
        
        elif mode == 5:
            print(f"\n{Fore.YELLOW}[*] Starting SSL/TLS Certificate Validation...{Style.RESET_ALL}")
            results['ssl_validation'] = ssl_certificate_check(url1, url2)
        
        elif mode == 6:
            print(f"\n{Fore.YELLOW}[*] Starting Vulnerability Scanning...{Style.RESET_ALL}")
            results['vulnerability_scan'] = vulnerability_scan(url1, url2)
        
        elif mode == 7:
            check_and_install_tools()
            return
        
        if output_file or results:
            export_results(results, url1, output_file)
        
        print(f"\n{Fore.GREEN}[+] Scan completed successfully!{Style.RESET_ALL}")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error during scan: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
