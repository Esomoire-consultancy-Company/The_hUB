from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, Replit!</h1></body></html>')

def get_ip():
    # This gets the IP address that other computers can use to connect to this server
    try:
        # Create a socket and connect to an external server
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "0.0.0.0"  # Fallback to listen on all interfaces

def run_server(port=5000):
    server_address = ('0.0.0.0', port)  # Listen on all interfaces
    ip = get_ip()
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running at http://{ip}:{port}/")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()