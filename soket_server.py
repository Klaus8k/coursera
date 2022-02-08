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

        self.transport.write(resp.encode())








loop = asyncio.get_event_loop()
coro = loop.create_server(ServerProtocol,'127.0.0.1',55555)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
