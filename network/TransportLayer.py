from . import time, cstr
import network.NetworkLayer as nl


def tcp_send(msg, client, server):
    print(f'>>\n>> {cstr("TRANSPORT LAYER", "cyan")}')
    print(f'>> {time()} Using TCP protocol')
    print(f'>> {time()} Sending message: {cstr(msg,"green")}')
    nl.route_packet(msg, client, server)
