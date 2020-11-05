import socket


class Server:
    def __init__(self, ip):
        super().__init__()
        self.ip = ip

    def listener(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("0.0.0.0", 3000))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data)


def send(ip, msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, 3000))
        s.sendall(msg.encode("UTF-8"))
