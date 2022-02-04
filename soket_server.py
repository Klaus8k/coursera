import socket

with socket.socket() as sock:
    sock.bind(("",20003))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        with conn:
            data = conn.recv(1024)
            if data:
                print(data.decode('utf-8'))
                conn.send(b'ok')
            else:
                conn.send(b'Erorr')

