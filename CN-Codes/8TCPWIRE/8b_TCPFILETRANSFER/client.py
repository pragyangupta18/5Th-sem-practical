import socket

# Define the server's IP and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

while True:
    print("Menu:")
    print("1. Send a file")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        filename = input("Enter the filename to send: ")
        client_socket.send(filename.encode())
        response = client_socket.recv(1024).decode()

        if response == "File not found":
            print(f"File '{filename}' not found on the server.")
        else:
            with open(f"received_{filename}", 'wb') as file:
                data = client_socket.recv(1024)
                while data:
                    file.write(data)
                    data = client_socket.recv(1024)
            print(f"File '{filename}' received successfully as 'received_{filename}'.")

    elif choice == '2':
        print('Goodbye!')
        client_socket.close()
        break

    else:
        print("Invalid choice. Please try again.")
