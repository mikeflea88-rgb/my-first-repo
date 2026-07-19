import socket
import sys
from datetime import datetime

# Define the target (You can use an IP address or domain name)
# We use localhost (127.0.0.1) as a safe default to test your own machine
TARGET = "127.0.0.1"

print("-" * 50)
print(f"[+] Scanning Target: {TARGET}")
print(f"[+] Scan Started at: {str(datetime.now())}")
print("-" * 50)

# A list of standard common ports to check:
# 21: FTP, 22: SSH, 23: Telnet, 25: SMTP, 80: HTTP, 443: HTTPS
common_ports = [21, 22, 23, 25, 80, 110, 143, 443, 3306, 8080]

try:
    for port in common_ports:
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a 1-second timeout so it doesn't hang forever on closed ports
        s.settimeout(1.0)
        
        # connect_ex returns an error indicator instead of throwing an exception
        result = s.connect_ex((TARGET, port))
        
        if result == 0:
            print(f"[!] Port {port:5}: OPEN")
        else:
            print(f"[-] Port {port:5}: Closed")
            
        s.close()

except KeyboardInterrupt:
    print("\n[-] Exiting script (Ctrl+C detected).")
    sys.exit()

except socket.gaierror:
    print("\n[-] Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\n[-] Could not connect to server.")
    sys.exit()

print("-" * 50)
print("[+] Port scan completed successfully.")
