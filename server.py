#
#|\_____|\
#|^ >o< ^|
#

from http.server import HTTPServer, BaseHTTPRequestHandler

paths = {
    '/bank'     : ( 'bank.html', 'file' ),
    '/balance'  : [ 100,         'text' ],
    '/cats'     : ( 'cats.html', 'file' ),
}

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = str(self.path)

        if path in paths:
            self.respond(path)

        else:
            #update balance (transfer submitted)
            try: paths['/balance'][0] -= int(path[15:])
            except: pass
            self.respond('/bank')

    def respond(self, path):
        self.send_response(200)
        self.end_headers()
        responce_data = lambda x: self.wfile.write(x.encode())
        data, type = paths[path]

        #file (html)
        if type == 'file':
            with open(data, "r") as f:
                responce_data(f.read())

        #text (balance)
        else: responce_data(str(data))


httpd = HTTPServer(('localhost', 8080), RequestHandler)
httpd.serve_forever()
