import socket


class Server:
    def __init__(self):
        self.connection = []
        self.messages = []
        self.HOST = self.get_local_ip()
        self.PORT = 1115

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('192.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def serverFunction(self, handler):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()

            while True:
                try:
                    conn, addr = s.accept()
                    with conn:
                        self.connection.append(conn)

                        while True:
                            data = conn.recv(1024).decode('utf-8')
                            self.messages.extend(data.split(';')[:-1])

                            while self.messages:
                                ms = self.messages.pop()

                                self.message_handler(ms, handler)


                except TimeoutError as e:
                    continue

                except OSError as e:
                    self.connection.pop()

    def send_message(self, message):
        for conn in self.connection:
            try:
                conn.send(message.encode('utf-8'))
            except:
                self.connection.pop()

    def message_handler(self, message, handler):
        print(f'Принято сообщение: {message}')
        if handler:
            handler(message)
