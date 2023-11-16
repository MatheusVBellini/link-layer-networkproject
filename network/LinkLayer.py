from collections import namedtuple
from binascii import crc32
from . import time, cstr

# framed packet structure
framedPacket = namedtuple('framedPacket', ['content'])


# frame the packet and send it through the physical connection
def frame_packet(packet, source, destination):
    print(f'>>\n>> {cstr("LINK LAYER - CLIENT", "cyan")}')
    print(f'>> {time()} Framing packet')

    bin_packet = packet.encode('utf-8')  # get packet bits
    uint_crc = crc_calc(bin_packet)  # get crc of the packet
    bin_crc = uint_crc.to_bytes(length=4, byteorder='big', signed=False)  # byte representation of the crc
    algorithm = 'flagbytes'  # define the framing algorithm to be Flag Bytes

    print(f'>> {time()} Packet (utf-8/bits): {cstr(packet, "green")} / {cstr(bytes_to_bits(bin_packet), "green")}')
    print(f'>> {time()} Calculated CRC-32 (uint/bits): {cstr(uint_crc, "green")} / {cstr(bytes_to_bits(bin_crc), "green")}')
    print(f'>> {time()} Framing algorithm: {cstr(algorithm, "green")}')

    framed_packet = frame(bin_crc + bin_packet)

    print(f'>> {time()} Framed packet: {cstr(bytes_to_bits(framed_packet), "green")}')
    return framed_packet, source, destination


# process received framed data (unframing and error detection)
def unpack_packet(packet, source, destination):
    print(f'>>\n>> {cstr("LINK LAYER - SERVER", "cyan")}')
    print(f'>> {time()} unframing packet')
    print(f'>> {time()} detecting errors')
    return packet, source, destination

# transform a string into a stream of bits
def bytes_to_bits(bin_data):
    return ''.join(f'{byte:08b}' for byte in bin_data)


# calculate the CRC polynomial
def crc_calc(packet):
    return crc32(packet)


# frame a packet
def frame(packet, algorithm='flagbytes'):
    if algorithm == 'flagbytes':
        return flagbytes(packet)


# calculate the odd parity bit of a byte stream
def odd_parity(packet):
    return (len(list(filter(lambda x: x == 1, packet))) % 2).to_bytes(length=1, byteorder='big', signed=False)


### framing algorithms ###
# sets a flag at the start and at the end of the packet to define its borders
def flagbytes(packet):
    flag = b'\x7e'
    return flag + packet + flag
