from . import time, cstr

def tcpSend(msg, client, server):
    print(f'>> {cstr("TRANSPORT LAYER","cyan")}')
    print(f'>> {time()} Using TCP protocol')
    print(f'>> {time()} Sending message: {msg}')