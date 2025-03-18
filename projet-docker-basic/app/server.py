from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Code HTTP 200 OK
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        message = "<html><body><h1>Hello, Docker!</h1></body></html>"
        self.wfile.write(message.encode("utf-8"))  # Envoi de la réponse HTML

if __name__ == "__main__":
    PORT = 8000
    server_address = ("0.0.0.0", PORT)  # Écoute sur tous les réseaux
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {PORT}...")
    try:
        httpd.serve_forever()  # Démarre le serveur indéfiniment
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()  # Arrêt propre du serveur
