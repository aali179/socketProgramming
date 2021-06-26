from binascii import hexlify
import socket

def main():
    #get datagram from client
    datagram = getDatagram()

    # total length: bytes 3-4
    totalLength = int(datagram[4:8], 16)
    # payload size = totalLength - 20 bytes (fixed header size)
    payloadSize = totalLength - 20
    # get payload HEX -> ASCII
    payload = bytearray.fromhex(datagram[40:].decode("ASCII")).decode()
    # get client IP
    clientIP = getClientIP(datagram[24:32].decode("ASCII"))

    # get 16 bit header fields for checksum verfication
    header = []
    for i in range(0, 40, 4):
        header.append(datagram[i:i+4].decode("ASCII"))

    # verify checksum
    if getChecksum(header) == "0000":
        verificationResult = "correct."
    else:
        verificationResult = "corrupted. Packet discarded!"

    print("The data received from", clientIP, "is", payload)
    print("The data has", payloadSize*8, "bits or", payloadSize, "bytes. Total length of packet is", totalLength, "bytes.")
    print("The verification of the checksum demonstrates that the packet received is", verificationResult)


def getClientIP(hexIP):
    bytes = ["".join(x) for x in zip(*[iter(hexIP)]*2)]
    bytes = [int(x, 16) for x in bytes]
    return ".".join(str(x) for x in bytes)

def getDatagram():
    # set up server socket and return datagram
    # localhost
    HOST = '192.168.2.88'
    # port to listen on
    PORT = 6000

    # using AF_INET as IPv4 internet address family, SOCK_STREAM for TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # associate socket with IP address and port number
        s.listen()  # enable server to accept connections
        conn, addr = s.accept()  # get client socket object from accept()
        with conn:
            while True:
                data = conn.recv(1024)  # get data from client
                return data

def getChecksum(header):
    # sum of 16 bit header fields
    sum = "0"
    for field in header:
        sum = hex(int(sum, 16) + int(field, 16))
    # wrap-sum by adding the carry-bit
    if len(sum) - 2 > 4:
        sum = int(sum[2], 16) + int(sum[3:], 16)

    # 1's complement
    checksum = '{:04X}'.format(int("FFFF", 16) - sum)
    return checksum

main()
