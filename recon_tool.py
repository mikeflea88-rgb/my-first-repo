import socket
import urllib.request
import sys

print("=" * 50)
print("             AUTOMATED OSINT & RECON TOOL        ")
print("=" * 50)

domain = input("Enter target domain (e.g., example.com): ").strip()

# Clean up input if user accidentally added http
if domain.startswith("http://"): domain = domain.replace("http://", "")
if domain.startswith("https://"): domain = domain.replace("https://", "")

print(f"\n[*] Target Domain: {domain}")
print("-" * 50)

# 1. IP Address Resolution
try:
    target_ip = socket.gethostbyname(domain)
    print(f"[+] Target IP Address: {target_ip}")
except socket.gaierror:
    print("[-] Error: Could not resolve IP address. Domain might be down or invalid.")
    sys.exit()

# 2. HTTP Header/Server Banner Grabbing
print("[*] Attempting HTTP banner grab...")
try:
    # Set a 3-second timeout so the script doesn't hang
    response = urllib.request.urlopen(f"http://{domain}", timeout=3)
    headers = response.info()
    
    # Extract specific interesting infrastructure headers
    server = headers.get("Server", "Unknown")
    powered_by = headers.get("X-Powered-By", "Hidden")
    
    print(f"[+] Web Server Software: {server}")
    print(f"[+] Application Tech:    {powered_by}")
except Exception as e:
    print(f"[-] Could not grab web headers: {e}")

print("-" * 50)
print("[+] Basic reconnaissance finished.")
