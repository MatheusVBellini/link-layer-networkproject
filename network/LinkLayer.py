from collections import namedtuple
from . import time, cstr

# framed packet structure
framedPacket = namedtuple('framedPacket', ['content'])

# frame the packet and send it through the physical connection
def framePacket(packet, source, destination):
    print(f'>>\n>> {cstr("DATA LINK LAYER","cyan")}')
    print(f'>> {time()} Framing packet from {source.ipv4} to {destination.ipv4}\n>>')
    