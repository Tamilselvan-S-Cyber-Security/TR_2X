# TR_2X (Threat Recon 2X) Usage Examples

**GitHub:** https://github.com/Tamilselvan-S-Cyber-Security/TR_2X

## Quick Start

### Interactive Mode
Launch the interactive menu to select scanning options:
```bash
python3 tr2x.py
```

### Check Tool Installation
Verify which external security tools are installed:
```bash
python3 tr2x.py -m 7
```
or
```bash
python3 tr2x.py --install
```

## Scanning Examples

### 1. Network Scanning
Scan for open ports and services:
```bash
python3 tr2x.py -u https://example.com -m 1
```

### 2. Bug Bounty Reconnaissance
Perform DNS enumeration and SSL validation:
```bash
python3 tr2x.py -u https://example.com -m 2
```

### 3. Comprehensive Penetration Test
Run network scanning and vulnerability detection:
```bash
python3 tr2x.py -u https://example.com -m 3
```

### 4. DNS Reconnaissance Only
Focus on DNS records and subdomain discovery:
```bash
python3 tr2x.py -u https://example.com -m 4
```

### 5. SSL/TLS Certificate Validation
Check certificate expiry, issuer, and security:
```bash
python3 tr2x.py -u https://example.com -m 5
```

### 6. Vulnerability Scanning
Test for XSS, SQLi, LFI, SSRF, Open Redirect, and CORS:
```bash
python3 tr2x.py -u https://example.com -m 6
```

## Advanced Usage

### Dual URL Scanning
Compare two targets simultaneously:
```bash
python3 tr2x.py -u https://example.com -u2 https://test.com -m 3
```

### Custom Output File
Save results with a custom filename:
```bash
python3 tr2x.py -u https://example.com -m 6 -o my_security_scan
```

### Multiple Scans with Results
```bash
# Network scan
python3 tr2x.py -u https://example.com -m 1 -o network_scan

# Vulnerability scan
python3 tr2x.py -u https://example.com -m 6 -o vuln_scan

# Results saved in results/ directory:
# - network_scan.txt
# - network_scan.json
# - vuln_scan.txt
# - vuln_scan.json
```

## Scanning Modes Reference

| Mode | Name | Description |
|------|------|-------------|
| 1 | Network Scanning | Port detection, service enumeration |
| 2 | Bug Bounty | DNS + SSL validation workflow |
| 3 | Penetration Testing | Comprehensive assessment |
| 4 | DNS Reconnaissance | DNS-focused scanning |
| 5 | SSL/TLS Validation | Certificate security analysis |
| 6 | Vulnerability Scanning | XSS, SQLi, LFI, SSRF, CORS testing |
| 7 | Tool Installation | Check external tools |

## Output Location
All scan results are saved in the `results/` directory with both `.txt` and `.json` formats.

## Important Notes
- Always obtain proper authorization before scanning any target
- Use this tool only for educational and authorized security testing
- Developed by CyberWolf Team for security professionals
