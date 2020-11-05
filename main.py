import logging
import argparse
import library.networking as net
import threading


ip = input(">")

con = net.Connection(ip)

cmd = input(">")

if cmd == "server":
    server = con.server()
    server()
else:
    cs, cl = con.client()
    x = threading.Thread(target=cl, args=())
    x.start()
    while True:
        msg = input("Msg: ")
        cs(msg)
