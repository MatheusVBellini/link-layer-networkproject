from collections import namedtuple
from binascii import crc32
from . import time, cstr
import network.PhysicalLayer as pl

# framed packet structure
framedPacket = namedtuple('framedPacket', ['content'])

even_parity = True


def setup_parity():
    global even_parity

    while True:
        parity_type = input('>> type which parity error checking you want: ')

        if parity_type == 'even':
            even_parity = True
            return
        if parity_type == 'odd':
            even_parity = False
            return
        print(
            f'>> {time()} invalid parity type selected, only "even" or "odd" accepted')

# frame the packet and send it through the physical connection


def frame_packet(packet, source, destination):
    print(f'>>\n>> {cstr("LINK LAYER - CLIENT", "cyan")}')

    setup_parity()

    print(f'>> {time()} Framing packet')

    bin_packet = packet.encode('utf-8')  # get packet bits
    uint_crc = crc_calc(bin_packet)  # get crc of the packet
    # byte representation of the crc
    bin_crc = uint_crc.to_bytes(length=4, byteorder='big', signed=False)
    bin_parity = parity(bin_packet, even_parity)  # returns a parity check byte

    algorithm = 'flagbytes'  # define the framing algorithm to be Flag Bytes

    print(f'>> {time()} Packet (utf-8/bits): {cstr(packet, "green")} / {cstr(bytes_to_bits(bin_packet), "green")}')
    print(
        f'>> {time()} Calculated CRC-32 (uint/bits): {cstr(uint_crc, "green")} / {cstr(bytes_to_bits(bin_crc), "green")}')
    print(f'>> {time()} Framing algorithm: {cstr(algorithm, "green")}')

    framed_packet = frame(bin_crc + bin_parity + bin_packet)

    print(
        f'>> {time()}   Framed packet: {cstr(bytes_to_bits(framed_packet), "green")}')

    pl.transport_packet(framed_packet, source, destination)


# process received framed data (unframing and error detection)
def unpack_packet(packet, source, destination):
    print(f'>>\n>> {cstr("LINK LAYER - SERVER", "cyan")}')

    print(f'>> {time()} Returned packet: {cstr(bytes_to_bits(packet), "green")}')

    unframed_packet = unframe(packet)

    # error detection
    print(f'>> {time()} Detecting errors:')

    received_crc = packet[1:5]  # what CRC currently is
    received_parity = packet[5:6]  # what the parity bit is
    calculated_crc = crc_calc(unframed_packet).to_bytes(
        length=4, byteorder='big', signed=False)  # what CRC should be
    # what parity bit should be
    calculated_parity = parity(unframed_packet, even_parity)

    if received_crc == calculated_crc:
        print(f'>> {time()} CRC {cstr("OK", "green")}')
    else:
        print(f'>> {time()} CRC {cstr("FAILED", "red")}')

    if received_parity == calculated_parity:
        print(
            f'>> {time()} {"Even" if even_parity else "Odd"} Parity Bit {cstr("OK", "green")}')
    else:
        print(
            f'>> {time()} {"Even" if even_parity else "Odd"} Parity Bit {cstr("FAILED", "red")}')

    destination.receive(unframed_packet)


# transform a string into a stream of bits
def bytes_to_bits(bin_data):
    return ''.join(f'{byte:08b}' for byte in bin_data)


# calculate the CRC polynomial
def crc_calc(packet):
    return crc32(packet)


# calculate the parity bit of a byte stream
def parity(packet, is_even=False):
    v = 1
    if is_even:
        v = 0
    return ((v + len(list(filter(lambda x: x == '1', bytes_to_bits(packet))))) % 2).to_bytes(length=1, byteorder='big',
                                                                                             signed=False)


# frame a packet
def frame(packet, algorithm='flagbytes'):
    if algorithm == 'flagbytes':
        return flagbytes(packet)


# unframe a packet
def unframe(packet, algorithm='flagbytes'):
    if algorithm == 'flagbytes':
        return undo_flagbytes(packet)
    else:
        raise ValueError("invalid algorithm argument for unframe")


# sets a flag at the start and at the end of the packet to define its borders
def flagbytes(packet):
    flag = b'~'
    return flag + packet + flag


# undo flagbytes frame
def undo_flagbytes(packet):
    if packet[-1] != ord('~') or packet[0] != ord('~'):
        print(f'>> {time()} flagbyte padding {cstr("FAILED", "red")}')
    else:
        print(f'>> {time()} flagbyte padding {cstr("OK", "green")}')

    return packet[6:-1]
