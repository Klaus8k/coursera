import socket
import time

# Реализоваить класс пользовательского исключения Клиент Ерор. А то даже первый тест не проходит)
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
        # print(data)
        try:
            self.sock.send(data.encode('utf-8'))
            req = self.sock.recv(1024)
        except BaseException as ClientError:
            raise ClientError

        req = req.decode('utf-8')
        req = req.split('\\n')[1:-2]
        # req.pop(0)
        # print(req) # Спсок из ответа, надо разобрать на словарь
        res_dict = dict()
        keys = []
        metrics = []
        for i in req:
            key = i.split()[0]
            x = i.split()[1:]
            x.reverse()
            tup_x = tuple(x)
            metrics.append(tup_x)
            if key in res_dict.keys():
                res_dict[key].append(tup_x)
            else:
                res_dict[key] = []
                res_dict[key].append(tup_x)
                # Sort list metrics
            for val in res_dict.values():
                val.sort()

        return res_dict


# if __name__ == '__main__':
#     x = Client('127.0.0.1', 20003)
#     # x.put("eardrum.memory", 4200000)
#     # x.put("eardrum.memory", 4200)
#     # x.get("eardrum.memory")
#     print(x.get('*'))
