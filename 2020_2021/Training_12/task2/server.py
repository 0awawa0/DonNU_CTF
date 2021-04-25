from http.server import BaseHTTPRequestHandler, HTTPServer
import random
from base64 import b64encode
import logging


class TaskServer(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def parse_args(self, path):
        s = path.split("?")
        if len(s) < 2: 
            return (s[0], {})

        args = s[1].split("&")
        args = {i.split("=")[0]: i.split("=")[1] for i in args}
        return (s[0], args)

    def do_GET(self):
        self._set_response()

        print(self.parse_args(self.path))
        path, args = self.parse_args(self.path)
        if path == "/get_flag":
            if "is_admin" in args and args["is_admin"] == "True":
                self.wfile.write(b"donnuCTF{0183f310f59590382c46526b9e34b127}")    
            else:
                self.wfile.write(b"You are not admin!")
        else:
            self.wfile.write(open("page.html", 'rb').read())


def run(server_class=HTTPServer, handler_class=TaskServer, port=43585):
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