from http.server import HTTPServer
from server import RequestHandler

def run_server():
    server_address = ("0.0.0.0", 3000)
    server = HTTPServer(server_address, RequestHandler)
    print(f"Server runs on {server_address[0]}:{server_address[1]}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()