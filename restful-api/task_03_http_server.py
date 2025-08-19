#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class HTTPhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            massage = "Hello, this is a simple API!"
            self.wfile.write(bytes(massage, "utf8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            massage = "OK"
            self.wfile.write(bytes(massage, "utf8"))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(bytes(data, "utf8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(bytes(data, "utf8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            massage = "Endpoint not found"
            self.wfile.write(bytes(massage, "utf8"))


server = HTTPServer(("", 80), HTTPhandler)
server.serve_forever()
server.server_close()
