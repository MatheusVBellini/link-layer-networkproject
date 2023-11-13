from network.ApplicationLayer import Client, Server

def main():
    client = Client()
    server = Server()
    blocked_client = Client()

    # setting the environment
    client.setMessage() # set a message to be sent

    # connection
    client.connect(server) # works and connects both
    blocked_client.connect(server) # fails and does not connect

    # sending
    blocked_client.send() # fails
    client.send() # works

if __name__ == '__main__':
    main()