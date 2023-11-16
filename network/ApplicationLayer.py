from . import time, cstr
import network.TransportLayer as tl
import network.NetworkLayer as nl
import network.LinkLayer as ll
import network.PhysicalLayer as pl


# mock client for proof of concept
class Client:

    # constructor
    def __init__(self):
        self.message = ''
        self.server = 0
        self.ipv4 = '192.168.0.1'

    # set a message to be sent
    def set_message(self):
        print(f'>>\n>> {cstr("APPLICATION LAYER", "cyan")}')
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
            print(f'>> {time()} Client is not connected to a server')
            return

        data = (self.message, self, self.server)
        data = tl.tcp_send(data[0], data[1], data[2])
        data = nl.route_packet(data[0], data[1], data[2])
        data = ll.frame_packet(data[0], data[1], data[2])
        data = pl.transport_packet(data[0], data[1], data[2])
        self.server.receive(data)


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
            self.client = client
            return True
        return False

    # receive data from client and proceed operation
    def receive(self, data):
        ll.unpack_packet(data[0], data[1], data[2])