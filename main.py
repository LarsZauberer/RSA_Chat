import library.networking as net
import threading
import sys

ip = sys.argv[1]

s = net.Server("127.0.0.1")
x = threading.Thread(target=s.listener, args=[])
x.start()
while True:
    msg = input("Msg: ")
    net.send(ip, msg)
