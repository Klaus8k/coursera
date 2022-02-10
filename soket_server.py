import socket
import threading
from multiprocessing import Queue

all_data = {}

def run_server(host,port):
    with socket.create_server((host,port)) as serv:
        while True:
            serv.settimeout(10)
            connect_socket(serv)

def connect_socket(serv):
    conn, addr = serv.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print('data recv ---------- ', data)

        data_list = data.decode().split('\n')
        print('data reuest ---------- ', data_list)
        data = []

        for i in data_list:
            if i != '':
                data.append(i)


        print('data reuest ---------- ', data)

        for j in data:
            i = j.split()
            if i[0] == 'put':
                try:
                    key, value, timestamp = i[1:]
                    value = float(value)
                    timestamp = int(timestamp)
                except:
                    result = 'error\nwrong command\n\n'

                result = put(key, value, timestamp)


            elif i[0] == 'get' and len(i) == 2:
                result = get(i[1])



            else:
                result = 'error\nwrong command\n\n'


            # print('response ---------- ', result)
            result += '\n'
            conn.send(result.encode())

    conn.close()
    return None

def put(key, value, timestamp):

    dic = {key: [(float(value), int(timestamp))]}
    if not key in all_data.keys():
        all_data.update(dic)
    else:
        all_data[key].append((float(value), int(timestamp)))

    for i in all_data.values():
        i.sort()
    print('all_data--------- ', all_data)
    print('put dic ----------- ', dic)
    return 'ok\n'

def get(row):
    responce = 'ok'
    print('get row -------------', row)
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
    print('get_responce ------ ', responce)
    return responce











if __name__ == '__main__':

    run_server('127.0.0.1', 8888)
