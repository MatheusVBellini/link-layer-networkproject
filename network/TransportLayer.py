from . import time, cstr
import network.NetworkLayer as nl

def tcpSend(msg, client, server):
    print(f'>>\n>> {cstr("TRANSPORT LAYER","cyan")}')
    print(f'>> {time()} Using TCP protocol')
    print(f'>> {time()} Sending message: {msg}')
    nl.routePacket(msg, client, server)
