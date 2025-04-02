from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, Replit!</h1></body></html>')

def run_server(port=8080):
    server_address = ('0.0.0.0', port)  # Listen on all interfaces
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running at http://0.0.0.0:{port}/")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()