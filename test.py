import asyncio

all_data = {}

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        super(ClientServerProtocol, self).__init__()
        # self.listen()
        # self.mess = mess


    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.listen(data)


    def send(self, data):
        self.transport.write(data)

    def listen(self, data):
        # while True:
        # data = b""
        # while not data.endswith(b"\n"):
        #     data += x

        i = data.decode().split()

        if i[0] == 'put':
            try:
                key, value, timestamp = i[1:]
                value = float(value)
                timestamp = int(timestamp)
            except:
                result = 'error\nwrong command\n\n'
            result = self.put(key, value, timestamp)

        elif i[0] == 'get' and len(i) == 2:
            if not all_data:
                result = 'ok\n'
            else:
                result = self.get(i[1])

        else:
            result = 'error\nwrong command\n\n'

        result += '\n'
        print(result)
        i = result.encode()
        self.send(i)

    def put(self, key, value, timestamp):
        dic = {key: [(float(value), int(timestamp))]}
        if not key in all_data.keys():
            all_data.update(dic)
        elif key in all_data.keys():
            for i in all_data[key]:
                if timestamp == i[1]:
                    all_data[key].pop()
            all_data[key].append((float(value), int(timestamp)))

        for i in all_data.values():
            i.sort()
        return 'ok\n'


    def get(self, row):
        responce = 'ok\n'

        try:
            if row == '*':
                for i in all_data.keys():
                    for j in all_data[i]:
                        responce += f'{i} {j[0]} {j[1]}\n'
            elif row in all_data.keys():
                for i in all_data[row]:
                    responce += f'{row} {i[0]} {i[1]}\n'
            else:
                responce = 'ok\n'

        except:
            return 'error\nwrong command\n'
        return responce


# Запуск асинхронного сервера
def run_server(host,port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == '__main__':

    run_server('127.0.0.1', 8888)
