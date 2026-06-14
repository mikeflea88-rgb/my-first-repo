from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

# Get your real WiFi IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

print(f"🔥 Zongo Dev Server LIVE!")
print(f"Tell friends: http://{ip}:8000")
print(f"Stop server: Ctrl+C")

HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler).serve_forever()
