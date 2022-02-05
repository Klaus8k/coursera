import socket

answer_str = r'ok\npalm.cpu 2.0 1150864248\npalm.cpu 0.5 1150864247\neardrum.cpu 3.0 1150864250\n\n'
answer_ok = r'ok\n\n'
with socket.socket() as sock:
    sock.bind(("",20003))
    sock.listen()

    while True:
        conn, addr = sock.accept()


        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except OSError:
                    continue
                if data:
                    print(data)
                    print(data.decode('utf-8'))
                    conn.send(answer_ok.encode('utf-8'))
                else:
                    break


