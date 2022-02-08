import asyncio
import socket

class ServerProtocol(asyncio.Protocol):
    """Запросы от клиента приходят в data_received(), после чего
    передаем в put() or get(). Там формируем ответ, возвращаем.
    Вопрос о сохранении данных для дальнейших ответов по ГЕТ"""


    def connection_made(self, transport) -> None:
        self.transport = transport
    def data_received(self, data: bytes) -> None:
        resp = data.decode()

        # Что то вот это не работает. Возвращает одно значение при этом не отправляет во write
        if resp.split()[0] == 'put':
            print(resp)
            responce = self.put(resp)
        elif resp.split()[0] == 'get':
            responce == self.get(resp)
        else: self.responce = 'error\nwrong command\n\n'

        self.transport.write(responce.encode())

    def put(self, request):
        print('put')
        return 'PUT'

    def get(self, request):
        print('get')
        return 'GET'







loop = asyncio.get_event_loop()
coro = loop.create_server(ServerProtocol,'127.0.0.1',8888)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
