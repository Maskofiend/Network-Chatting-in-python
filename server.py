import socket
from datetime import datetime

def start_server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('0.0.0.0', 5555))

    s.listen(5)

    print("Server is listening on 0.0.0.0:5555")

    conn, addr = s.accept()

    print(f"connected by {addr}")

    current_time = datetime.now().strftime("%H:%M:%S")
    
    username = conn.recv(1024).decode()

    connection_successful_msg = f"Welcome! {username}"

    conn.send(connection_successful_msg.encode())


    while True:


        data = conn.recv(1024)

        if data == b'':
            break
        
        message = data.decode()
        print(f"{current_time} {username}: {message}")

        reply = input("You: ")

        conn.send(reply.encode())
    
        
    
if __name__ == "__main__":
    start_server()