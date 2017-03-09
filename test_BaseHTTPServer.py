#coding:utf8
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json

class TodoHandler(BaseHTTPRequestHandler):
    TODOS = []
    def do_GET(self):
        if self.path != "/":
            self.send_error(404, "File not found")
            return
        message = json.dumps(self.TODOS)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(message)

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers["content-type"])
        print self.headers
        if ctype == "application/json":
            length = int(self.headers["content-length"])
            post_values = json.loads(self.rfile.read(length))
            self.TODOS.append(post_values)
        else:
            self.send_error(415, "Only json data is supported.")
            return

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(post_values)

if __name__ == "__main__":
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(("localhost", 8888), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()

