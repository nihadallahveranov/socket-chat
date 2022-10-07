import socket, threading

def client() -> None:
    '''
        Main Thread that start client connection to the server 
        and handle it's input messages
    '''

    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 9999

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        threading.Thread(target=handle_messages, args=(socket_instance,)).start()

        print('Connected successfully')

        while True:
            msg = input()

            if msg == 'exit':
                break

            socket_instance.send(msg.encode())

        socket_instance.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


def handle_messages(connection: socket.socket):
    '''
        Receive messages sent by the server and display them to user
    '''

    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break

if __name__ == "__main__":
    client()