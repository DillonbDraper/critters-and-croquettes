from land_animals import *
from slimy_animals import *
from water_animals import *
from http.server import BaseHTTPRequestHandler, HTTPServer

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()