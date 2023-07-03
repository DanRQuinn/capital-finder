from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.headers.add_header('Content-type', 'text/plain')
        self.end_headers()

        message = "Hello, world!\n"

        self.wfile.write(message.encode())

        return
