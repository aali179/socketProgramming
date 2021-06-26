from binascii import hexlify
import socket


def main(serverIP, payload):
    # convert payload ASCII to HEX
    payloadHex = hexlify(payload.encode('ascii'))
    # header fields
    bytes1_2 = "4500"
    totalLength = '{:04X}'.format((int(20 + len(payloadHex) / 2)))
    id = "1C46"
    flag = "4000"
    TTL_TCP = "4006"
    checksum = "0000"
    serverIPHex = getIP(serverIP)
    clientIP = getIP(socket.gethostbyname(socket.gethostname())) # get client IP of machine

    header = [bytes1_2, totalLength, id, flag, TTL_TCP, checksum, clientIP[:4], clientIP[4:], serverIPHex[:4], serverIPHex[4:]]
    # set checksum
    header[5] = getChecksum(header)

    HOST = serverIP  # server IP address
    PORT = 6000  # port used by server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for field in header:
            s.sendall(field.encode())
        s.sendall(payloadHex)


def getIP(serverIP):
    return '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, serverIP.split(".")))


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


serverIP = input("Server IP:")
payload = input("Payload:")
main(serverIP, payload)
