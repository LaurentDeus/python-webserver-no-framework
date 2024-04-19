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

        if self.path.endswith('/delete'):   

            id = self.path.split('/')[-2]
            restaurant_name = get_restaurant(id)

            if delete_restaurant(id):
                self.send_response(302)
                self.send_header('location', '/restaurants')
                self.end_headers()
            else:
                resp = f'''<h1 style='color:red'> failed to Delete {restaurant_name} Restaurant</h1>'''
                self.send_response(500)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write(resp.encode())


        elif self.path.endswith('/edit'):
            id = self.path.split('/')[-2]
            form = cgi.FieldStorage(self.rfile, self.headers, environ={
                                    'REQUEST_METHOD': self.command, 'CONTENT_TYPE': self.headers['content_type']})
            new_restaurant_name = form.getvalue('restaurant_name')

            if update_restaurant_name(id, new_restaurant_name):
                self.send_response(302)
                self.send_header('location', '/restaurants')
                self.end_headers()
            else:
                resp = f'''<h1 style='color:red'> failed to Edit to {restaurant_name} Restaurant</h1>'''
                self.send_response(500)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write(resp.encode())

        elif self.path.endswith('/restaurant/new'):
            # print(self.headers)
            form = cgi.FieldStorage(self.rfile, self.headers, environ={'REQUEST_METHOD': self.command,
                                                                       'CONTENT_TYPE': self.headers['Content-Type'],
                                                                       })

            restaurant_name: str = form.getvalue('restaurant_name', '')
            if create_restaurant(restaurant_name):
                self.send_response(302)
                self.send_header('location', '/restaurants')
                self.end_headers()
            else:
                resp = f'''<h1 style='color:red'> failed to create {restaurant_name} Restaurant</h1>'''
                self.send_response(500)
                self.send_header('content-type', 'text/html')
                self.end_headers()
                self.wfile.write(resp.encode())

    def do_GET(self):

        if self.path.endswith('/delete'):
            id = self.path.split('/')[-2]
            restaurant = get_restaurant(id)
            self.send_headers_for_success_GET()
            out = f"""<h2 style='color:red'>Do Your Really Want to delete {restaurant.name} Restaurant</h2>
            <form method="post">
    <input type="submit" value="Delete">
</form>          
            """
            self.wfile.write(out.encode())

        elif self.path.endswith('/edit'):
            id = self.path.split('/')[-2]
            self.send_headers_for_success_GET()
            restaurant = get_restaurant(id)

            out = f"""<h2>Editing {restaurant.name} Restaurant</h2>
            <form method="post">
    <input type="text" name="restaurant_name" placeholder="{restaurant.name}" ><br><br>
    <input type="submit" value="Rename">
</form>          
            """
            self.wfile.write(out.encode())

        elif self.path.endswith('/restaurant/new'):
            self.send_headers_for_success_GET()
            out = """<h1>CREATING NEW RESTAURANT</h1>
<form action="/restaurant/new" method="post">
    <input type="text" name="restaurant_name" placeholder='Restaurant Name'><br><br>
    <input type="submit" value='Create'>
</form>"""
            self.wfile.write(out.encode())

        elif self.path.endswith('/restaurants'):
            # print(self.headers)
            # print(self.path)
            self.send_headers_for_success_GET()

            output = "<h1>RESTAURANTS</h1><h3><a href='/restaurant/new'>Create New Restaurant Here</a></h3>"
            all_restaurants = get_all_restaurants()
            for r in all_restaurants:
                output += f"""<h2>{r.name}</h2><a href='/restaurant/{r.id}/edit'>Edit</a><br>
<a href='/restaurant/{r.id}/delete'>Delete</a><br><br>"""

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
