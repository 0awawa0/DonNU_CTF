from http.server import BaseHTTPRequestHandler, HTTPServer
import random
from base64 import b64encode
import logging


class Task1Server(BaseHTTPRequestHandler):

    @staticmethod
    def generatePage():
        page = """
<!DOCTYPE html>
<html>
<head>
    <title>Task 1</title>
</head>
<body style="background: #384534;">

"""
        trueFlag = b64encode("donnuCTF{w3b1_tru3_flag_44328}".encode())
        trueFlagIndex = random.randint(50, 950)
        for i in range(1000):
            if i != trueFlagIndex:
                fakeFlag = b64encode(("donnuCTF{fak3_f1ag_" + str(random.randint(2**16, 2**32)) + "}").encode())
                page += f"<button style=\"margin: 10px; padding: 5px;\" onclick=\"alert('Nope! {fakeFlag.decode()}');\">Give me the flag!</button>\n"
            else:
                page += f"<button style=\"margin: 10px; padding: 5px;\" onclick=\"alert('Nope! {trueFlag.decode()}');\">Give me the flag!</button>\n"
            if not (i + 1) % 5:
                page += "<br>"
        page += "</body>\n</html>"
        return page

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(Task1Server.generatePage().encode())


def run(server_class=HTTPServer, handler_class=Task1Server, port=43584):
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