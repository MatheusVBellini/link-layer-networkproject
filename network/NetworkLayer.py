from . import time, cstr

def routePacket(packet, source, destination):
    print(f'>>\n>> {cstr("NETWORK LAYER","cyan")}')
    print(f'>> {time()} Routing packet from {source.ipv4} to {destination.ipv4}\n>>')