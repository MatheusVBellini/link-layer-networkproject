from . import time, cstr
import network.LinkLayer as ll


def route_packet(packet, source, destination):
    print(f'>>\n>> {cstr("NETWORK LAYER - CLIENT", "cyan")}')
    print(f'>> {time()} Routing packet from {cstr(source.ipv4,"green")} to {cstr(destination.ipv4, "green")}')
    ll.frame_packet(packet, source, destination)
