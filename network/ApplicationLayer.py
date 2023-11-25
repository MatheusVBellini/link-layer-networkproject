from . import time, cstr
import network.TransportLayer as tl

# mock client for proof of concept
class Client:

    # constructor
    def __init__(self, ipv4):
        self.message = ''
        self.server = None
        self.ipv4 = ipv4
        print(f'>> {time()} Client {cstr(self.ipv4, "green")} initialized')

    # set a message to be sent
    def set_message(self):
        self.message = input('>>\n>> Type your message here: ')
        print('>>')

    # Attempt to connect to server
    def connect(self, server):
        if self.server is not None:
            print(f'>> {time()} Client {cstr(self.ipv4, "green")} already ' +
                  'connected to this or another server')

            print(f'>> {time()} Connection could not be completed\n>>')
            return False
        if server.connect(self):
            self.server = server
            print(f'>> {time()} Client {cstr(self.ipv4, "green")}' +
                  ' connected to server\n>>')

            return True
        print(f'>> {time()} Connection to {cstr(self.ipv4, "green")} could ' +
              'not be completed:')

        print(f'>> {time()} Server {cstr(server.ipv4, "green")} is busy\n>>')
        return False

    # send message to server
    def send(self):
        if self.server is None:
            print(f'>> {time()} Client {cstr(self.ipv4, "green")} is not ' +
                  'connected to a server')

            return

        print(f'>> {time()} Client {cstr(self.ipv4, "green")} started ' +
              'sending the message')

        data = (self.message, self, self.server)
        tl.tcp_send(data[0], data[1], data[2])


# mock server for proof of concept
class Server:

    # constructor
    def __init__(self, ipv4):
        self.client = None
        self.ipv4 = ipv4
        print(f'>> {cstr("APPLICATION LAYER", "cyan")}\n>>')
        print(f'>> {time()} Server {cstr(self.ipv4, "green")} initialized')

    # accept or deny client request to connect

    def connect(self, client):
        if self.client is None:
            self.client = client
            return True
        return False

    # receive data from client and proceed operation
    def receive(self, data):
        print(f'>>\n>> {cstr("APPLICATION LAYER - SERVER", "cyan")}')

        message = data
        try:
            message = data.decode()
        except UnicodeDecodeError:
            print(f'>> {time()} Server {cstr(self.ipv4, "green")} received' +
                  ' an invalid UTF-8 message!')

        print(f'>> {time()} Server {cstr(self.ipv4, "green")} received ' +
              f'message: {message}')
