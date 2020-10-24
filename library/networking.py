import logging
import socket

log = logging.getLogger("Connection")


class Connection:
    def __init__(self, ip):
        """Connection class

        Args:
            ip (str): The ip to connect to
        """
        assert type(ip) == str
        self.ip = ip
        self.port = '4234'
        log.info(f"Created connection object with ip: {self.ip}")

    def send(self, msg):
        """Send a message

        Args:
            msg (list): message splited in chars
        """
        assert type(msg) == list
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.port))
            log.debug(f"Sending message {msg}")
            for index, item in enumerate(msg):
                log.debug(f"Sending message package {index}")
                s.sendall(item.decrypt('UTF-8'))
            log.info(f"Message sent")

    def receive(self):
        """Receive a message

        Returns:
            list: The message as a list in bytes
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            while True:
                s.bind((self.ip, self.port))
                s.listen()
                conn, addr = s.accept()
                log.info(f"Found connection")
                with conn:
                    data = []
                    while True:
                        new_data = conn.recv(1024)
                        data.append(new_data)
                        log.debug(f"Received package {len(data)}")
                        if not new_data:
                            break
                    log.info(f"All data received!")
                    return data
