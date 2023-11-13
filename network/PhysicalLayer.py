from . import time, cstr


# moves the data physically, generating statistical noise and errors in the data
def transport_packet(packet, source, destination):
    print(f'>>\n>> {cstr("PHYSICAL LAYER", "cyan")}')
    print(f'>> {time()} Moving packet from one point to another...')
