__author__ = 'Lonja'
import socket, time

UDP_IP = "127.0.0.1"
UDP_PORT = 9999


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print ("received message:", data)
        print (addr)
        #data = b'hello:'+ data
        rtnStr = "python has heard".ljust(1024)
        time.sleep(3)
        sock.sendto((rtnStr.encode("utf-8") ), addr)
    except :
        pass