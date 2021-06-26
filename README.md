# Socket Programming in Python
Transmitting IPv4 packets from client to server using sockets in Python.

Afrah Ali 300049798 - Zoha Sajjad 300018688

## Description
### PacketSender
The client program which takes `serverIP` and `payload` input from the user to send to server socket. 
The function `getChecksum(header)` calculates the 16-bit checksum from the header fields.
The payload is concatenated to the header and sent through to the server on port 6000.

## PacketReceiver
The server program which receives the datagram from the socket and verifies the checksum.

*NOTE: The server socket is hardcoded to run on 192.168.2.88. If you wish to direct the packet to a different server IP, this can be set on line 41 of `PacketReceiver`.*

## Setup
0. (Optional) Set desired server IP address in line 41 of `PacketReceiver.py` to overwrite the default socket address '192.168.2.88'

    `HOST = '192.168.2.88'`

2. Run `PacketReceiver.py` in a terminal window:

`python3 PacketReceiver.py`

2. In a new terminal window, run `PacketSender.py`:

`python3 PacketSender.py`

3. Enter the server IP address or the default 192.168.2.88 and payload. The packet verfication results will be displayed in the first terminal. 
