import os, http.server, socketserver
os.chdir(os.path.join(os.path.dirname(__file__), 'src'))
PORT = 3000
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
