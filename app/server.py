from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import asyncio
from utility.scanner import scan
from utility.http_request import http_request

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/scan":
            self.handle_scan_request()
        elif self.path == "/sendhttp":
            self.handle_sendhttp_request()
        else:
            self.send_error(404, "Endpoint not found")

    def handle_scan_request(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = self.parse_json(post_data)

            network = data.get("network")
            verbose = data.get("verbose")
            if not network:
                raise ValueError("Missing 'network' field")

            response = asyncio.run(scan(network, verbose))
            self.respond_with_json(200, response)
        
        except ValueError as e:
            self.respond_with_error(400, str(e))

    def handle_sendhttp_request(self):
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = self.parse_json(post_data)

            header_key = data.get("Header")
            header_value = data.get("Header-value")
            target = data.get("Target")
            method = data.get("Method")
            payload = data.get("Payload")

            if not all([header_key, header_value, target, method]):
                raise ValueError("Error: Missing required fields")
            
            headers = {header_key: header_value}
            response = http_request(target, method, headers=headers, payload=payload)
            self.respond_with_json(200, response)
        
        except ValueError as e:
            self.respond_with_error(400, str(e))

    def parse_json(self, data):
        try:
            return json.loads(data.decode('utf-8'))
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON")

    def respond_with_json(self, status_code, payload):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = json.dumps(payload, indent=4)
        self.wfile.write(response.encode('utf-8'))

    def respond_with_error(self, status_code, message):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        error_response = {"error": message}
        self.wfile.write(json.dumps(error_response).encode('utf-8'))
