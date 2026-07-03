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
    
    while True:
        data = conn.recv(1024)

        if data == b'':
            break
        
        message = data.decode()
        print(f"{current_time} Client: {message}")

        reply = input("You: ")

        conn.send(reply.encode())
    
        #print("sent message!")
    
if __name__ == "__main__":
    start_server()