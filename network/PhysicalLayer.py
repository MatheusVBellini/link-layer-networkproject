from . import time, cstr
import random as r
import network.LinkLayer as ll

# moves the data physically, generating statistical noise and errors in the data
def transport_packet(packet, source, destination):
    print(f'>>\n>> {cstr("PHYSICAL LAYER", "cyan")}')
    print(f'>> {time()} Moving packet from one point to another...')

    packet_out = bytes()
    for i, byte_in in enumerate(packet):
        byte_out = transport_byte(i, byte_in)
        packet_out += byte_out

    ll.unpack_packet(packet_out, source, destination)

def transport_byte(pos, value_in):
    value_out = 0

    # for each bit
    for i in range(8):
        # try to transport it, or fail
        if r.randint(0, 99) != 0:
            value_out |= value_in & (1 << i)
        else:
            value_out |= (value_in ^ 0b11111111) & (1 << i)
            print(f'>> {time()} flipped bit {i} of byte {pos}')

    return value_out.to_bytes(length=1, byteorder='big', signed=False)
