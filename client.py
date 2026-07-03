import socket
from datetime import datetime

def start_connection():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    c.connect(('127.0.0.1', 5555))

    print("Connected!")

    current_time = datetime.now().strftime("%H:%M:%S")

    while True:
        

        reply = input("You: ")

        c.send(reply.encode())



        data = c.recv(1024)

        if data == b'':
            break
        message = data.decode()
        print(f"{current_time} Server: {message}")

if __name__ == "__main__":
    start_connection()