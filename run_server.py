import http.server
import socketserver
import os

# Define the port you want to use
PORT = 8080

# This is a good practice to find out which IP address and port the server is using.
# It helps to know if you have any firewall issues.
def get_local_ip():
    """Try to get the local IP address."""
    try:
        # Connect to an external host to find the local IP.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1" # Fallback to localhost

# Change to the directory where the script is located
# This ensures the server can find your index.html and other files.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except Exception:
    pass # Stay in current directory if it fails

# Create a simple request handler
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
# Using (host, port) makes it accessible on your local network, not just localhost
httpd = socketserver.TCPServer((get_local_ip(), PORT), Handler)

print(f"""
========================================
✅ Deriv Worm Engine Server Active ✅
========================================
🌐 Server running on: http://{get_local_ip()}:{PORT}
🌐 Or locally at: http://localhost:{PORT}
📁 Serving files from: {os.getcwd()}
========================================
Press Ctrl+C to stop the server.
""")

# Start the server
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 Server stopped by user.")
    httpd.server_close()

