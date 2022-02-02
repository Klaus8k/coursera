import socket


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

    def put(self, data: str):  # Здесь отправляем значения, ничего не возвращаем если удачно
        self.sock.send(data.encode('utf-8'))  # Отправка в байткоде или декодером, подготовленного сообщения, по сигнатуре. Вроде можно через енкод в ютф 8

    def get(self, name_metrics):
        pass
        # Сюда имя метрики которую мы хотим получить от сервера.

    def close_conn(self):  # Посмотреть как закрывать соединения
        self.sock.shutdown(0)


if __name__ == '__main__':
    x = Client('127.0.0.1', 20003)
    data = x.__doc__
    x.put(data)
    x.close_conn()
