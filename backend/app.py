from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!\n")

HTTPServer(("0.0.0.0", PORT), SimpleHandler).serve_forever()
