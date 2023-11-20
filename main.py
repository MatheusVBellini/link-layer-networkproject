from network.ApplicationLayer import Client, Server


def main():
    server = Server('189.46.2.121')
    client = Client('192.168.0.1')
    blocked_client = Client('10.0.0.1')

    # setting the environment
    client.set_message()  # set a message to be sent

    # connection
    client.connect(server)  # works and connects both
    blocked_client.connect(server)  # fails and does not connect

    # sending
    blocked_client.send()  # fails
    client.send()  # works


if __name__ == '__main__':
    main()
