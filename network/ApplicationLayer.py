# mock client for proof of concept
class Client:

    # constructor
    def __init__(self):
        self.message = ''
        self.server = 0
    
    # set a message to be sent
    def setMessage(self):
        print('>> Client initialized')
        self.message = input('>> Type your message here: ')
        print('>>')

    # Attempt to connect to server
    def connect(self, server):
        if self.server != 0:
            print('>> Client already connected to this or another server')
            print('>> Connection could not be completed\n>>')
            return False
        if server.connect(self):
            self.server = server
            print('>> Client connected to server\n>>')
            return True
        print('>> Server is busy')
        print('>> Connection could not be completed\n>>')
        return False

# mock server for proof of concept
class Server:

    # constructor
    def __init__(self):
        self.message = 'NO_MESSAGE_RECEIVED'
        self.client = 0

    # accept or deny client request to connect
    def connect(self, client):
        if self.client == 0:
            self.free = False
            self.client = client
            return True
        return False
            