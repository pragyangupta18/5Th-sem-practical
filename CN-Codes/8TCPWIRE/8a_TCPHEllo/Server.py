import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 8000)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is waiting for connections...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Client: {data}")

        # Menu for the server
        print("1. Send a message")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Server: ")
            client_socket.send(message.encode('utf-8'))
        elif choice == "2":
            print('Good Bye!')
            break
        else:
            print("Invalid choice. Please try again.")

    except KeyboardInterrupt:
        break

# Close the sockets
client_socket.close()
server_socket.close()


#Client


# import socket

# # Create a socket object
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Define the server address and port to connect to
# server_address = ('localhost', 12345)

# # Connect to the server
# client_socket.connect(server_address)
# print("Connected to the server.")

# while True:
#     try:
#         # Menu for the client
#         print("1. Send a message")
#         print("2. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             # Send a message to the server
#             message = input("Client: ")
#             client_socket.send(message.encode('utf-8'))

#             # Receive a response from the server
#             response = client_socket.recv(1024).decode('utf-8')
#             print(f"Server: {response}")
#         elif choice == "2":
#             print('Good Bye!')
#             break
#         else:
#             print("Invalid choice. Please try again.")
#     except KeyboardInterrupt:
#         break

# # Close the socket
# client_socket.close()
