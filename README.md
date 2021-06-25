# Socket Programming in Python
Transmitting IPv4 packets from client to server using sockets in Python.

Afrah Ali 300049798 - Zoha Sajjad 300018688

## Description
### PacketSender
The client program which takes `serverIP` and `payload` input from user to send to server socket. 
The function `getChecksum(header)` calculates the 16-bit checksum from the header fields.
The payload is concatenated to the header and sent through to the server on port 6000.

The program assumes that the client and server machines are the same and running on 192.168.2.88

## PacketReceiver
The server program which receives the datagram from the socket and verifies the checksum. The socket is running on 192.168.2.88 and port 6000.

## Setup
1. Run `PacketReceiver.py` in a terminal window:

`python3 PacketReceiver.py`

2. In a new terminal window, run `PacketSender.py`:

`python3 PacketSender.py`

3. Enter the server IP address and payload. The server socket is hardcoded to run on 192.168.2.88 and port 6000. The packet verfication results will be displayed in the first terminal. 
