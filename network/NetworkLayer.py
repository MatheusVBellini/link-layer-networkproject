from . import time, cstr


def route_packet(packet, source, destination):
    print(f'>>\n>> {cstr("NETWORK LAYER - CLIENT", "cyan")}')
    print(f'>> {time()} Routing packet from {cstr(source.ipv4,"green")} to {cstr(destination.ipv4, "green")}')
    return packet, source, destination
