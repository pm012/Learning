from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse


class HttpGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = parse.urlparse(self.path)
        match url.path:
            case '/':
                self.send_response(200, "Hello from index")

def run (server_class = HTTPServer, handler_class = HttpGetHandler):
    server_address = ('', 8000)
    http = server_class(server_address, handler_class)
    try: 
        http.serve_forever()
    except:
        http.server_close()


if __name__ == "__main__":
    run()