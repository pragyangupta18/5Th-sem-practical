import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port to connect to
server_address = ('localhost', 8000)

# Connect to the server
client_socket.connect(server_address)
print("Connected to the server.")

while True:
    try:
        # Menu for the client
        print("1. Send a message")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Send a message to the server
            message = input("Client: ")
            client_socket.send(message.encode('utf-8'))

            # Receive a response from the server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server: {response}")
        elif choice == "2":
            print('Good Bye!')
            break
        else:
            print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        break

# Close the socket
client_socket.close()
