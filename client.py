import socket
from datetime import datetime

def start_connection():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    c.connect(('127.0.0.1', 5555))

    print("Connected!")

    current_time = datetime.now().strftime("%H:%M:%S")

    username = input("Enter your username: ")

    c.send(username.encode())

    server_message = c.recv(1024)

    start_server_message = server_message.decode()

    print(start_server_message)
    
    

### Connect! message sent but does not start the enter your username bug

    while True:
    

        reply = input(f"{username}: ")

        c.send(reply.encode())



        data = c.recv(1024)

        if data == b'':
            break
        message = data.decode()
        print(f"{current_time} Server: {message}")

if __name__ == "__main__":
    start_connection()