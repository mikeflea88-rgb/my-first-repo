import socket
import sys
import threading
from queue import Queue
from datetime import datetime

TARGET = "127.0.0.1"

print("-" * 50)
print(f"[+] Launching High-Speed Threaded Scanner on: {TARGET}")
print(f"[+] Scan Started at: {str(datetime.now())}")
print("-" * 50)

# Create a queue to hold all the ports we want to scan
port_queue = Queue()

# Fill the queue with ports (let's check the first 1024 standard ports this time!)
for port in range(1, 1025):
    port_queue.put(port)

# Lock prevents multiple threads from printing and overlapping text on the screen
print_lock = threading.Lock()

def scan_worker():
    while not port_queue.empty():
        # Get the next port number out of the queue
        port = port_queue.get()
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5) # Fast 0.5 second timeout
            
            result = s.connect_ex((TARGET, port))
            
            if result == 0:
                with print_lock:
                    print(f"[!] Port {port:5}: OPEN")
                    
            s.close()
            
        except Exception:
            pass
            
        # Tell the queue that this port task is finished
        port_queue.task_done()

# Define how many threads (workers) to deploy
# 100 threads means 100 ports are checked simultaneously!
NUMBER_OF_THREADS = 100
thread_list = []

# Spawn and start the threads
for _ in range(NUMBER_OF_THREADS):
    t = threading.Thread(target=scan_worker)
    t.daemon = True # Allows script to exit cleanly on Ctrl+C
    thread_list.append(t)
    t.start()

# Wait for all ports in the queue to be processed before finishing
port_queue.join()

print("-" * 50)
print(f"[+] Scan completed at: {str(datetime.now())}")
print("[+] All 1024 ports scanned successfully.")
