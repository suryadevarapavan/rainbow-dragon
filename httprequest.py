import socket
from html.parser import HTMLParser

HOST = 'www.google.com'  # Server hostname or IP address
PORT = 80                # The standard port for HTTP is 80, for HTTPS it is 443

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
client_socket.connect(server_address)

request_header = b'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
client_socket.sendall(request_header)

response = ''
while True:
    recv = client_socket.recv(1024)
    if not recv:
        break
    response += recv.decode('utf-8')
class Parsering(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print("start tag:",tag)
    def handle_endtag(self,tag):
        print("start tag:",tag)
    def handle_data(self,data):
        print("start tag:",data)
parser =  Parsering()
parser.feed(response)
#print(response)
client_socket.close()
