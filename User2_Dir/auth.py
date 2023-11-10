import socket
import random

with open("seed-increment.txt", 'r') as seed_file:
    seed, increment = seed_file.read().split(' ')

def connect_to_server(message):
    global seed, increment

    server_address = ('127.0.0.1', 450)

    client_socket = socket.socket()

    try:
        client_socket.connect(server_address)

        client_socket.send(message.encode())

        response = client_socket.recv(128).decode()
        print("Server Response:", response)

        if response == 'Success!':
            with open("seed-increment.txt", 'w') as seed_file:
                seed_file.write(f'{seed} {increment+1}')

    finally:

        client_socket.close()

# Example usage:
username = input('Enter your username: ')
password = input('Enter your password: ')
increment = int(increment)
seed = int(seed)

random.seed(seed)

for i in range(increment):
    random.randint(100000000000, 999999999999)

seed_value = random.randint(100000000000, 999999999999)

message = f"{username}/{password}/{seed_value}"

# Connect to the server and send the message
connect_to_server(message)
