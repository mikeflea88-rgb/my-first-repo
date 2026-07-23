import socket
import datetime

print("=== SECURITY LAB DASHBOARD v1.0 ===")
print("WARNING: This only scans 127.0.0.1 - YOUR OWN DEVICE")
print("")

def port_scan_local():
    target = "127.0.0.1"
    print(f"Scanning {target} at {datetime.datetime.now()}")
    open_ports = []
    
    # Only scan common dev ports for safety
    ports = [22, 80, 443, 8080, 3000, 5000]
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
        s.close()
    
    if not open_ports:
        print("No open dev ports found")
    else:
        print(f"\nFound {len(open_ports)} open port(s) on your device")

def system_log():
    print("\n=== SYSTEM LOG ===")
    print(f"Scan Time: {datetime.datetime.now()}")
    print("Target: 127.0.0.1 ONLY")
    print("Status: Safe Lab Mode")

while True:
    print("\n1. Run Local Port Scan")
    print("2. Show System Log")
    print("3. Exit")
    choice = input("Pick: ")
    
    if choice == "1":
        port_scan_local()
    elif choice == "2":
        system_log()
    elif choice == "3":
        print("Exiting Lab. Stay safe CEO")
        break
    else:
        print("Invalid choice")
