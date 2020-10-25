import logging
import socket

log = logging.getLogger("Connection")


class Connection:
    def __init__(self, ip, port="4234"):
        """Connection class

        Args:
            ip (str): The ip to connect to
        """
        # Assert parameters
        assert type(ip) == str
        assert len(ip) > 0
        assert type(port) == str
        assert len(port) > 0

        # Assigne variables
        self.ip = ip
        self.port = port
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
                s.sendall(bytes(item))
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
                    print(data)


def listen(con, ip="0.0.0.0", port="4234"):
    """Listen to all ip connections

    Args:
        ip (str, optional): The ip to listen to. Defaults to "0.0.0.0".
        port (str, optional): The port to listen to. Defaults to "4234".

    Returns:
        str: Address which connectedtd
    """
    # Parameter assertion
    assert type(ip) == str
    assert len(ip) > 0
    assert type(port) == str
    assert len(port) > 0

    # Search for connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        log.info(f"Start searching a connection")
        s.bind(ip, port)
        conn, addr = s.accept()
        log.info(f"Found a connection: {addr}")
        con = Connection(addr)


def connect(ip, port="4234"):
    """Connect to a ip

    Args:
        ip (str): Ip to connect to
        port (str, optional): Port of the program. Defaults to "4234".
    """
    # Parameter assertion
    assert type(ip) == str
    assert len(ip) > 0
    assert type(port) == str
    assert len(port) > 0

    # Start a connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(b"start connection")


def ip_input(con_variable):
    """Input field for the ip

    Args:
        con_variable (Connection variable): where the connection will be stored

    """
    print("IP to connect:")
    ip = input()
    connect(ip)
    con_variable = Connection(ip)
