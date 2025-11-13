from urllib.parse import urlparse
from colorama import Fore, Style
import sys

def validate_url(url):
    if not url:
        return None
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        parsed = urlparse(url)
        if not parsed.netloc:
            print(f"{Fore.RED}[!] Invalid URL: {url}{Style.RESET_ALL}")
            sys.exit(1)
        return url
    except Exception as e:
        print(f"{Fore.RED}[!] Error validating URL: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

def extract_domain(url):
    try:
        parsed = urlparse(url)
        return parsed.netloc.replace('www.', '')
    except:
        return url
