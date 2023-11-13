from collections import namedtuple
from . import time, cstr

# framed packet structure
framedPacket = namedtuple('framedPacket', ['content'])


# frame the packet and send it through the physical connection
def frame_packet(packet, source, destination):
    print(f'>>\n>> {cstr("DATA LINK LAYER", "cyan")}')
    print(f'>> {time()} Framing packet from {cstr(source.ipv4,"green")} to {cstr(destination.ipv4, "green")}')
