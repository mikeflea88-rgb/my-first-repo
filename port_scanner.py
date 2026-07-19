import socket
import sys
from datetime import datetime

print("=" * 50)
print("             LIGHTWEIGHT PORT SCANNER            ")
print("=" * 50)

# Target input
target_input = input("Enter target IP or Domain (e.g., 192.168.1.1): ")

try:
    target_ip = socket.gethostbyname(target_input)
except socket.gaierror:
    print("\n[-] Error: Could not resolve hostname. Exiting.")
    sys.exit()

print(f"\n[+] Scanning Target: {target_ip}")
print(f"[+] Scan started at: {str(datetime.now())}\n" + "-" * 50)

# Common penetration testing ports to scan quickly
common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]

for port in common_ports:
    # Setup socket with 1 second timeout so it stays fast
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    
    # Try connecting to the port
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"[ OPEN ] Port {port:5} is open!")
    s.close()

print("-" * 50 + "\n[+] Scan finished successfully.")
