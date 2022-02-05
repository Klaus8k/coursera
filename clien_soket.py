import socket
import time


class Client():
    """
    Класс слиент, соединяется с сокетом по адресу
    и обладает методами отправки метрик и приема их.
    Держит соединение
    """

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((host, port), timeout)

    def put(self, name_and_metric: str, value: float, timestamp=int(time.time())):
        data = f'put {name_and_metric} {value} {timestamp}\\n'
        try:
            self.sock.send(data.encode('utf-8'))
            print(self.sock.recv(1024).decode('utf-8'))
        except BaseException as ClientError:
            print(data, ' - Fail')
            raise ClientError

    def get(self, name_and_metrics: str):
        data = f'get {name_and_metrics}\\n'
        print(data)
        try:
            self.sock.send(data.encode('utf-8'))
            req = self.sock.recv(1024)
        except BaseException as ClientError:
            raise ClientError
        print(req.decode('utf-8'))




if __name__ == '__main__':
    x = Client('127.0.0.1', 20003)
    # x.put("eardrum.memory", 4200000)
    # x.put("eardrum.memory", 4200)
    # x.get("eardrum.memory")
    x.get('*')
