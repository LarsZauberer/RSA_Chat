# Imports
import logging
import argparse
import multiprocessing
import library.networking as net


if __name__ == "__main__":
    # Log object
    log = logging.getLogger()

    con = None

    # Connection listener
    log.debug(f"Create listener process")
    first_cont = multiprocessing.Process(target=net.listen, args=(con,))
    first_cont.start()

    # Connect to
    log.debug(f"Create connect process")
    ip_input = multiprocessing.Process(target=net.ip_input, args=(con,))
    ip_input.start()

    while True:
        if con is not None:
            log.info(f"Connected to the ip: {con.ip}")
            try:
                first_cont.terminate()
                ip_input.terminate()
            except Exception as e:
                log.warning(f"Error while terminating threads")
                log.warning(f"{e}")
            break

    listener = multiprocessing.Process(target=con.receive)

    while True:
        msg = list(input(">"))
        for index, item in msg:
            msg[index] = int(chr(item))
        con.send(msg)
