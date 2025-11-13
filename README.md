# TR_2X (Threat Recon 2X) - Advanced Penetration Testing Tool

<p align="center">
  <img src="favicon.ico" alt="CyberWolf Logo" width="140" height="140" style="border-radius:50%; border:2px solid #1f2937;">
</p>

<p align="center"><strong>Developed by CyberWolf Team</strong></p>

[![GitHub](https://img.shields.io/badge/GitHub-TR__2X-blue?logo=github)](https://github.com/Tamilselvan-S-Cyber-Security/TR_2X)

TR_2X (Threat Recon 2X) is a comprehensive command-line penetration testing and bug bounty reconnaissance tool designed for security researchers and ethical hackers.

## 🔗 Links
- **GitHub Repository:** [https://github.com/Tamilselvan-S-Cyber-Security/TR_2X](https://github.com/Tamilselvan-S-Cyber-Security/TR_2X)
- **Developer:** CyberWolf Team

## Features

- **Network Scanning** - Port detection, service enumeration, and host discovery
- **DNS Reconnaissance** - DNS records, subdomain discovery, zone transfer testing
- **SSL/TLS Validation** - Certificate analysis, expiry checks, and security validation
- **Vulnerability Scanning** - XSS, SQLi, LFI, SSRF, Open Redirect, and CORS testing
- **Bug Bounty Mode** - Automated workflows for bug bounty hunting
- **Dual URL Support** - Compare and scan two targets simultaneously
- **Export Results** - Save scan results in TXT and JSON formats

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Make TR_2X Executable

```bash
chmod +x tr2x.py
```

### 3. Install External Tools (Optional but Recommended)

Run the tool installer to check and get installation instructions:

```bash
python3 tr2x.py --install
```

## Usage

### Interactive Mode

```bash
python3 tr2x.py
```

### Command-Line Mode

```bash
# Scan a single URL
python3 tr2x.py -u https://example.com -m 1

# Scan two URLs
python3 tr2x.py -u https://example.com -u2 https://test.com -m 3

# Export results
python3 tr2x.py -u https://example.com -m 6 -o my_scan
```

### Scanning Modes

1. **Network Scanning** - Port and service detection
2. **Website Bug Bounty** - DNS recon + SSL validation
3. **Penetration Testing** - Comprehensive security assessment
4. **DNS Reconnaissance** - DNS enumeration and subdomain discovery
5. **SSL/TLS Certificate Validation** - Certificate security analysis
6. **Vulnerability Scanning** - XSS, SQLi, LFI, SSRF, CORS, etc.
7. **Install Required Tools** - Check and install external tools

## Command-Line Options

```
-u, --url       Primary target URL
-u2, --url2     Secondary target URL (optional)
-m, --mode      Scanning mode (1-7)
-o, --output    Output file path
--install       Check and install required tools
```

## Output

Results are automatically saved in the `results/` directory with:
- **TXT format** - Human-readable report
- **JSON format** - Machine-readable data for integration

## External Tools (Optional)

TR_2X works standalone but can leverage these tools for advanced features:

- **subfinder** - Fast subdomain discovery
- **nuclei** - Template-based vulnerability scanner
- **httpx** - HTTP toolkit
- **amass** - Attack surface mapping
- **gau** - URL gathering
- **nmap** - Network scanner
- **wpscan** - WordPress scanner

## Disclaimer

This tool is for **educational and authorized testing purposes only**. Always obtain proper authorization before testing any target. The CyberWolf Team is not responsible for misuse of this tool.

## Credits

**Developed by CyberWolf Team**

For bug bounty hunters, penetration testers, and security researchers.


## Developer Collaborations

<table align="center">
  <tr>
    <td align="center">
      <img src="https://www.cyberwolf.pro/images/1747757610488-photoaidcom-cropped.png" alt="Tamilselvan" width="80" height="80" style="border-radius:50%; border:2px solid #1f2937;"><br>
      <sub><strong>Tamilselvan</strong></sub>
    </td>
    <td align="center">
      <img src="https://cyberwolf-technology.web.app/cyberwolf_staffs/pugazhmani.jpg" alt="Pugazhmani" width="80" height="80" style="border-radius:50%; border:2px solid #1f2937;"><br>
      <sub><strong>Pugazhmani</strong></sub>
    </td>
    <td align="center">
      <img src="https://cyberwolf-technology.web.app/cyberwolf_staffs/arun-modified.png" alt="Arun" width="80" height="80" style="border-radius:50%; border:2px solid #1f2937;"><br>
      <sub><strong>Arun</strong></sub>
    </td>
    <td align="center">
      <img src="https://cyberwolf-technology.web.app/cyberwolf_staffs/Jayaboomika.jpg" alt="Jayaboomika" width="80" height="80" style="border-radius:50%; border:2px solid #1f2937;"><br>
      <sub><strong>Jayaboomika</strong></sub>
    </td>
    <td align="center">
      <img src="https://www.cyberwolf.pro/ramya/ramya.jpeg" alt="Ramya" width="80" height="80" style="border-radius:50%; border:2px solid #1f2937;"><br>
      <sub><strong>Ramya</strong></sub>
    </td>
  </tr>
</table>

<p align="center">
  <sub>CyberWolf Core Collaboration Team</sub>
</p>

