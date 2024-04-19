# remember servers are made on top of scokets
# so you need server_address and port

from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
from cruds import *


class HttpRequestHandler(BaseHTTPRequestHandler):

    def send_headers_for_success_GET(self):
        self.send_response(200, message='success')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # print(self.headers)
        form = cgi.FieldStorage(self.rfile, self.headers, environ={'REQUEST_METHOD': 'POST',
                                                                   'CONTENT_TYPE': self.headers['Content-Type'],
                                                                   })

        # print(form.getvalue('say'))
        say = form.getvalue('say', '')
        resp = f'''
<h2>Oooh Sure!!</h2>
<h1>{say}</h1>
<form action="" method="post">
    <label for="say"><strong>SAY</strong>:</label>
    <input type="text" name="say" id="say"><br><br>
    <input type="submit">
</form>
'''
        self.send_response(404)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(resp.encode())

    def do_GET(self):

        if self.path.endswith('/restaurants'):
            # print(self.headers)
            # print(self.path)
            self.send_headers_for_success_GET()

            output = '<h1>I Have Below Restaurants in My Database</h1>'
            for r in restaurants_names:
                output += f"""<h2>{r}</h2><a href=''>Edit</a><br>
<a href=''>Delete</a><br><br>"""

            self.wfile.write(output.encode())
        else:
            self.send_error(404, f'{self.path} not Found,Please check')
            # self.send_headers_for_success_GET()
            # self.wfile.write(
    #     "<h1 style='color:red'>I have no this Route, please wait :)</h1>".encode())


def main(server_class=HTTPServer, handler_class=HttpRequestHandler):

    try:
        server_name = 'localhost'
        server_port = 8000
        server_address = (server_name, server_port)
        httpd = server_class(server_address, handler_class)
        print(f'Server is Running at {server_name}:{server_port}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C entered, stopping the server')
        httpd.socket.close()


if __name__ == '__main__':
    main()
