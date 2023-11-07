import os
import socket


# Server and client functions
def start_server(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    print(f"Server listening on {server_ip}:{server_port}")
    while True:
        data, client_address = server_socket.recvfrom(1024)
        if data.decode() == "EXIT":
            break
        with open("received_file", "wb") as file:
            while True:
                data, _ = server_socket.recvfrom(1024)
                if data == b"EOF":
                    break
                file.write(data)
    server_socket.close()
    print("File received successfully.")

def start_client(client_ip, client_port, server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto("CONNECT".encode(), (server_ip, server_port))

    menu = """
    Menu:
    1. Send Script
    2. Send Text
    3. Send Audio
    4. Send Video
    5. Exit
    """

    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == "1":
            send_file(client_socket, client_ip, client_port, server_ip, server_port, "script.txt")
        elif choice == "2":
            send_file(client_socket, client_ip, client_port, server_ip, server_port, "text.txt")
        elif choice == "3":
            send_file(client_socket, client_ip, client_port, server_ip, server_port, "audio.mp3")
        elif choice == "4":
            send_file(client_socket, client_ip, client_port, server_ip, server_port, "video.mp4")
        elif choice == "5":
            print("Good bye!")
            client_socket.sendto("EXIT".encode(), (server_ip, server_port))
            break
        else:
            print("Invalid choice. Try again.")

def send_file(client_socket, client_ip, client_port, server_ip, server_port, filename):
    try:
        with open(filename, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.sendto(data, (server_ip, server_port))
                data = file.read(1024)
            client_socket.sendto(b"EOF", (server_ip, server_port))
        print(f"{filename} sent successfully.")
    except FileNotFoundError:
        print(f"{filename} not found.")

if __name__ == "__main__":
    server_ip = "127.0.0.1"  # Change this to the server's IP
    server_port = 12345  # Change this to the server's port
    client_ip = "127.0.0.1"  # Change this to the client's IP
    client_port = 54321  # Change this to the client's port

    role = input("Enter 'server' or 'client': ")
    if role == "server":
        start_server(server_ip, server_port)
    elif role == "client":
        start_client(client_ip, client_port, server_ip, server_port)
    else:
        print("Invalid role. Use 'server' or 'client'.")
