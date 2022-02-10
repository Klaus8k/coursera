import socket
import time


class ClientError(Exception):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((host, port), timeout)

    def put(self, name_and_metric: str, value: float, timestamp=None):
        if not timestamp:
            timestamp = int(time.time())

        data = f'put {name_and_metric} {value} {timestamp}\n'
        try:
            self.sock.send(data.encode('utf-8'))
            responce = self.sock.recv(1024)
            print(responce)
            if responce.decode('utf-8') != 'ok\n\n':
                raise ClientError
        except:
            raise ClientError


    def get(self, name_and_metrics: str):
        data = f'get {name_and_metrics}\n'
        try:
            self.sock.send(data.encode('utf-8'))
            req = self.sock.recv(4096)
        except:
            raise ClientError

        req = req.decode('utf-8')
        answer = req.split('\n')


        if answer[0] != 'ok':
            raise ClientError

        elif req == 'ok\n\n':
            return {}
        # import pdb
        # pdb.set_trace()

        req = answer[1:-2]
        res_dict = dict()
        metrics = []

        for i in req:

            try:
                key = str(i.split()[0])
                x = i.split()[1:]

                timestamp = int(float(x[1]))
                metric_value = float(x[0])
                tup_x = timestamp,metric_value,
                metrics.append(tup_x)
            except:
                raise ClientError

            if key in res_dict.keys():
                res_dict[key].append(tup_x)
            else:
                res_dict[key] = []
                res_dict[key].append(tup_x)
                # Sort list metrics
            for val in res_dict.values():
                val.sort()

        return res_dict





if __name__ == '__main__':
    x = Client('127.0.0.1', 8888)
    x.put("eardrum.memory", 4200000, 5)
    # print(x.get('*'))
