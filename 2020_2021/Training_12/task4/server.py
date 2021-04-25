from http.server import BaseHTTPRequestHandler, HTTPServer
from http import cookies
import random
from base64 import b64encode
import logging


class TaskServer(BaseHTTPRequestHandler):

    def setCSSHeaders(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/css')
        self.end_headers()    	

    def setPNGHeaders(self):
    	self.send_response(200)
    	self.send_header("Content-type", "image/png")
    	self.end_headers()

    def setHTMLHeaders(self):
        cookie = cookies.SimpleCookie()
        cookie["secret"] = "cWJhYWhQR1N7cjdzN3FzMjAyM284cm85MXMwMzM3ODMwczM5MjdyNjF9"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header("Set-Cookie", cookie.output(header=""))
        self.end_headers()    	

    def parse_args(self, path):
        s = path.split("?")
        if len(s) < 2: 
            return (s[0], {})

        args = s[1].split("&")
        args = {i.split("=")[0]: i.split("=")[1] for i in args}
        return (s[0], args)

    def do_GET(self):

        path, args = self.parse_args(self.path)
        if path == "/styles.css":
            self.setCSSHeaders()
            self.wfile.write(open("styles.css", 'rb').read())
        elif path == "/logo.png":
        	self.setPNGHeaders()
        	self.wfile.write(open("logo.png", 'rb').read())
        else:
            self.setHTMLHeaders()
            self.wfile.write(open("page.html", 'rb').read())


def run(server_class=HTTPServer, handler_class=TaskServer, port=43587):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting server\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Server stopped\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()