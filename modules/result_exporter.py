import json
from datetime import datetime
from colorama import Fore, Style
import os

def export_results(results, url, output_file=None):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if not os.path.exists('results'):
        os.makedirs('results')
    
    if not output_file:
        safe_url = url.replace('://', '_').replace('/', '_').replace(':', '_')
        output_file = f"results/scan_{safe_url}_{timestamp}"
    else:
        output_file = f"results/{output_file}"
    
    txt_file = f"{output_file}.txt"
    json_file = f"{output_file}.json"
    
    with open(txt_file, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("TR_2X (Threat Recon 2X) - Penetration Testing Report\n")
        f.write("Developed by CyberWolf Team\n")
        f.write("GitHub: https://github.com/Tamilselvan-S-Cyber-Security/TR_2X\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Target URL: {url}\n")
        f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 70 + "\n\n")
        
        f.write(format_results_text(results))
    
    with open(json_file, 'w') as f:
        scan_data = {
            'tool': 'TR_2X (Threat Recon 2X)',
            'developer': 'CyberWolf Team',
            'github': 'https://github.com/Tamilselvan-S-Cyber-Security/TR_2X',
            'target': url,
            'timestamp': timestamp,
            'scan_date': datetime.now().isoformat(),
            'results': results
        }
        json.dump(scan_data, f, indent=2)
    
    print(f"\n{Fore.GREEN}[+] Results exported:{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}├─ Text Report: {txt_file}{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}└─ JSON Report: {json_file}{Style.RESET_ALL}")
    
    return {'txt': txt_file, 'json': json_file}

def format_results_text(results, indent=0):
    output = []
    indent_str = "  " * indent
    
    if isinstance(results, dict):
        for key, value in results.items():
            if isinstance(value, (dict, list)):
                output.append(f"{indent_str}{key}:")
                output.append(format_results_text(value, indent + 1))
            else:
                output.append(f"{indent_str}{key}: {value}")
    elif isinstance(results, list):
        for item in results:
            if isinstance(item, (dict, list)):
                output.append(format_results_text(item, indent))
            else:
                output.append(f"{indent_str}- {item}")
    else:
        output.append(f"{indent_str}{results}")
    
    return "\n".join(output)
