import socket
import threading
import time
import asyncio

all_data = {}


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(connect_socket, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


async def connect_socket(reader, writer):
    print(writer.is_closing())

    while True:
        timme = int(time.time())

        data = b""
        print('enter time ---- ', round(time.time() - timme))
        while not data.endswith(b"\n"):
            try:
                data += await reader.read(1024)
            except:
                writer.close()
                await writer.wait_closed()

        # print('START data reuest ---- ', data, round(time.time() - timme, 1))

        i = data.decode().split()

        if i[0] == 'put':

            try:
                key, value, timestamp = i[1:]
                value = float(value)
                timestamp = int(timestamp)
            except:
                result = 'error\nwrong command\n\n'
            # print('time put ---- ', round(time.time() - timme, 1))

            result = put(key, value, timestamp)


        elif i[0] == 'get' and len(i) == 2:
            if not all_data:
                result = 'ok\n'
            else:
                result = get(i[1])

        else:
            result = 'error\nwrong command\n\n'

        result += '\n'
        i = result.encode()
        # print('response and END ---- ', i, round(time.time() - timme, 1))
        writer.write(i)
        await writer.drain()
        # https: // docs.python.org / 3.6 / library / asyncio - stream.html
        print('response and END ---- ', i, round(time.time() - timme))



    # writer.close()

def put(key, value, timestamp):
    # print('time 1 ---- ', (timme))
    dic = {key: [(float(value), int(timestamp))]}

    if not key in all_data.keys():
        all_data.update(dic)
    elif key in all_data.keys():
        for i in all_data[key]:
            if timestamp == i[1]:
                all_data[key].pop()
                # return 'ok\n'
        all_data[key].append((float(value), int(timestamp)))

    for i in all_data.values():
        i.sort()
    # print('all_data---- ', all_data)
    # print('put dic ---- ', dic)
    # print('time 2 ----', (datetime.time() - timme))
    return 'ok\n'


def get(row):
    responce = 'ok\n'
    # print('get row ----', row)

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
    # print('get_responce ---', responce[:-1])
    return responce


if __name__ == '__main__':
    run_server('127.0.0.1', 8888)
