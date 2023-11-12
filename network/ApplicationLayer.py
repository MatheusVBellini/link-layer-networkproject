from . import time, cstr
import network.TransportLayer as tl

# mock client for proof of concept
class Client:

    # constructor
    def __init__(self):
        self.message = ''
        self.server = 0
        self.ipv4 = '192.168.0.1'
    
    # set a message to be sent
    def setMessage(self):
        print(f'>>\n>> {cstr("APPLICATION LAYER","cyan")}')
        print(f'>> {time()} Client initialized')
        self.message = input('>> Type your message here: ')
        print('>>')

    # Attempt to connect to server
    def connect(self, server):
        if self.server != 0:
            print(f'>> {time()} Client already connected to this or another server')
            print(f'>> {time()} Connection could not be completed\n>>')
            return False
        if server.connect(self):
            self.server = server
            print(f'>> {time()} Client connected to server\n>>')
            return True
        print(f'>> {time()} Server is busy')
        print(f'>> {time()} Connection could not be completed\n>>')
        return False
    
    # send message to server
    def send(self):
        if self.server == 0:
            print(f'>> {time()} Client is not connected to a server\n>>')
            return
        tl.tcpSend(self.message, self, self.server)

# mock server for proof of concept
class Server:

    # constructor
    def __init__(self):
        self.message = 'NO_MESSAGE_RECEIVED'
        self.client = 0
        self.ipv4 = '189.46.2.121'

    # accept or deny client request to connect
    def connect(self, client):
        if self.client == 0:
            self.free = False
            self.client = client
            return True
        return False
            