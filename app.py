from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"<h1>Versione 2.1 - Deploy automatico riuscito!</h1>")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print("Server attivo sulla porta 8080...")
    server.serve_forever()