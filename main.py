import logging
import argparse
import library.networking as net


ip = input(">")

con = net.Connection(ip)

cmd = input(">")

if cmd == "server":
    con.receive()
else:
    con.send([65])
