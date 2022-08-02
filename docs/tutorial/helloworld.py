import time
import http.server
import os


HOST_NAME = '0.0.0.0' # Host name of the http server
# Gets the port number from $PORT0 environment variable
PORT_NUMBER = int(os.environ['PORT0'])


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Time Server</title></head>".encode())
        self.wfile.write(f"<body><p>The current time is {time.asctime()}</p>".encode())
        self.wfile.write("</body></html>".encode())

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), f"Server Starts - {HOST_NAME}:{PORT_NUMBER}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), f"Server Stops - {HOST_NAME}:{PORT_NUMBER}")
