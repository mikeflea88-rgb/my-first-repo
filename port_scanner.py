import socket
import sys
import threading
from queue import Queue
from datetime import datetime

print("=" * 50)
print("             INTERACTIVE THREADED SCANNER          ")
print("=" * 50)

# Ask the user for input
user_input = input("[?] Enter target IP address or hostname to scan: ").strip()

if not user_input:
    print("[-] Error: No target provided. Exiting.")
    sys.exit()

try:
    # Resolve hostname to target IP address
    TARGET = socket.gethostbyname(user_input)
except socket.gaierror:
    print(f"\n[-] Error: Hostname '{user_input}' could not be resolved.")
    sys.exit()

print("-" * 50)
print(f"[+] Launching High-Speed Scanner on: {TARGET} ({user_input})")
print(f"[+] Scan Started at: {str(datetime.now())}")
print("-" * 50)

# Create a queue to hold all the ports we want to scan
port_queue = Queue()

# Fill the queue with the first 1024 standard ports
for port in range(1, 1025):
    port_queue.put(port)

# Lock prevents multiple threads from printing and overlapping text
print_lock = threading.Lock()

def scan_worker():
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) 
            
            result = s.connect_ex((TARGET, port))
            
            if result == 0:
                with print_lock:
                    print(f"[!] Port {port:5}: OPEN")
                    
            s.close()
        except Exception:
            pass
            
        port_queue.task_done()

# Define threads
NUMBER_OF_THREADS = 100
thread_list = []

for _ in range(NUMBER_OF_THREADS):
    t = threading.Thread(target=scan_worker)
    t.daemon = True
    thread_list.append(t)
    t.start()

# Wait for queue to empty
port_queue.join()

print("-" * 50)
print(f"[+] Scan completed at: {str(datetime.now())}")
print("[+] All 1024 ports processed.")
