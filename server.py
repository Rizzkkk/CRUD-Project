import http.server

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


        with open('index.html', 'rb') as file:
            html_content = file.read()


        self.wfile.write(html_content)

def run():
    server_address = ('', 8000)  
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    print('Server running at http://localhost:8000/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
