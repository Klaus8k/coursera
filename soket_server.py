import socket
import threading
from multiprocessing import Queue

all_data = {}

def run_server(host,port):
    with socket.create_server((host,port)) as serv:
        while True:
            connect_socket(serv)

def connect_socket(serv):
    conn, addr = serv.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break

        data = data.decode().split()
        if data.pop(0) == 'put':
            result = put(data)
            print(all_data)
        else:
            result = get(data)
            print(all_data)



        conn.send(result.encode())

    conn.close()

def put(row):

    key, value, timestamp = row
    dic = {key: [(float(value), int(timestamp))]}
    if not key in all_data.keys():
        all_data.update(dic)
    else:
        all_data[key].append((float(value), int(timestamp)))

    for i in all_data.values():
        i.sort()

    return 'ok\n\n'

def get(data):


    return 'ok\n\n'



if __name__ == '__main__':

    run_server('127.0.0.1', 8888)
