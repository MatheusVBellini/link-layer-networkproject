from . import time, cstr


def tcp_send(msg, client, server):
    print(f'>>\n>> {cstr("TRANSPORT LAYER - CLIENT", "cyan")}')
    print(f'>> {time()} Using TCP protocol')
    print(f'>> {time()} Sending message: {cstr(msg,"green")}')
    return msg, client, server
