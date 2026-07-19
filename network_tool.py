import subprocess
import os

print("=" * 50)
print("     KALI AUTOMATION SUITE: NETWORK & PRIVACY     ")
print("=" * 50)

def change_mac():
    print("\n[+] Preparing to spoof MAC address...")
    interface = input("Enter network interface (e.g., wlan0, eth0): ")
    new_mac = input("Enter new MAC address (or press Enter for random): ")
    
    # Bring interface down, change MAC, bring it back up
    print(f"[-] Disabling {interface}...")
    subprocess.run(["sudo", "ip", "link", "set", interface, "down"])
    
    if new_mac:
        print(f"[-] Setting MAC to {new_mac}...")
        subprocess.run(["sudo", "macchanger", "-m", new_mac, interface])
    else:
        print("[-] Generating and setting random MAC...")
        subprocess.run(["sudo", "macchanger", "-r", interface])
        
    subprocess.run(["sudo", "ip", "link", "set", interface, "up"])
    print("[+] MAC address change sequence complete!")

def network_scan():
    print("\n[+] Preparing local network scan...")
    ip_range = input("Enter IP range to scan (e.g., 192.168.1.0/24): ")
    print(f"[-] Running Nmap ping scan on {ip_range}...")
    # Runs a quick ping scan to find alive hosts without taking too long
    subprocess.run(["sudo", "nmap", "-sn", ip_range])

# Main Menu
print("1. Spoof/Change MAC Address")
print("2. Scan Local Network (Discover Alive Hosts)")
choice = input("\nSelect an option (1 or 2): ")

if choice == "1":
    change_mac()
elif choice == "2":
    network_scan()
else:
    print("[-] Invalid choice. Exiting script.")
