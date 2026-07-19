import socket
import struct
import sys

try:
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
except Exception as e:
    print(f"[-] Failed to open socket: {e}")
    sys.exit()

print("[+] Sniffer active. Monitoring interface traffic...")
print("[*] Press Ctrl+C to stop sniffing and see totals.")
print("-" * 50)

# Counters for traffic analysis
stats = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}

try:
    while True:
        # Capture the raw binary packet data from the air
        raw_data, addr = sniffer.recvfrom(65535)
        
        # Unpack the Ethernet header (first 14 bytes)
        eth_header = raw_data[:14]
        eth = struct.unpack('!6s6sH', eth_header)
        eth_protocol = socket.ntohs(eth[2])
        
        # Protocol 8 means IPv4 traffic
        if eth_protocol == 8:
            # Unpack the IP header data
            ip_header = raw_data[14:34]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            protocol_type = iph[6] # The protocol ID byte
            
            # Identify the specific packet types
            if protocol_type == 6:
                stats["TCP"] += 1
                print("[!] Captured: TCP Packet detected.")
            elif protocol_type == 17:
                stats["UDP"] += 1
                print("[?] Captured: UDP Data Stream packet detected.")
            elif protocol_type == 1:
                stats["ICMP"] += 1
                print("[*] Captured: ICMP (Ping) request/reply detected.")
            else:
                stats["Other"] += 1

except KeyboardInterrupt:
    # Beautiful readout when you hit stop
    print("\n\n" + "=" * 50)
    print("              TRAFFIC CAPTURE SESSION SUMMARY      ")
    print("=" * 50)
    for proto, count in stats.items():
        print(f" -> {proto:8} Packets Intercepted: {count}")
    print("=" * 50)
    print("[+] Capture session ended clean.")
