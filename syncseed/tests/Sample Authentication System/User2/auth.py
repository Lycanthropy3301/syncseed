# Import the required libraries.
import numpy as np
import socket
import logging
import syncseed.syncseed as syncseed
from randomgen import ChaCha

# Import and unpack the config file
with open('..\\Config\\options.cfg') as config_file:
    config_options = {key[0].strip(): value.strip() for line in config_file if (key := line.split('=', 1)) and '[' not in key[0] and key[0].strip() for value in key}

# Unpack the Seed_Value challenge upper and lower bounds and number of challenge rounds. These must be consistent with both the server and client.
SEED_VALUE_LOWER_BOUND = int(config_options['SEED_VALUE_LOWER_BOUND'])
SEED_VALUE_UPPER_BOUND = int(config_options['SEED_VALUE_UPPER_BOUND'])
CHALLENGE_ROUNDS = int(config_options['CHALLENGE_ROUNDS'])
SEED_LENGTH = int(config_options['SEED_LENGTH'])

# Declare the server address to connect to.
SERVER_IP_ADDRESS = '127.0.0.1'

# Set up a basic logging system
logging.basicConfig(filename='client.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')

# Load the seed value stored locally client-side from a text file. In a production system, these would be stored more securely.
with open("seed-increment.txt", 'r') as seed_file:
    seed = int(seed_file.read().strip())


# Function to connect to the server 'main.py'. Does not return anything.
def connect_to_server(message, seed_value):

    # Set up a tuple with the server address and port (450 in this case).
    server_address = (SERVER_IP_ADDRESS, 450)

    # Initialise the client socket.
    client_socket = socket.socket()

    # Basic exception handling. Catches errors and logs them.
    try:
        # Connect to the server.
        client_socket.connect(server_address)

        # Send the message with authentication information.
        client_socket.send(message.encode())

        # Recieve a response from the server. Decodes this message (converts it to a string) and log it.
        response = client_socket.recv(512).decode()
        logging.info(f"Server Response: {response}")

        # Also, print the authentication message.
        print(f"Server Response: {response}")

        if response == 'Succeeded!':

            # If the server indicates that authentication is succesful, update the client-side seed increment in 'seed-incrment.txt'.

            new_seed = syncseed_generator.update_seed()

            with open("seed-increment.txt", 'w') as seed_file:
                seed_file.write(f'{new_seed}')

    # Exception handling as aforementioned.
    except Exception as exception:
        logging.error(f"Unexpected error: {str(exception)}")

    finally:

        # Log the client exit.
        logging.info("CLient shutting down.")

        # Close the client socket after receiving a server resonse or after an exception is encountered.
        client_socket.close()

# Main function.
def main():

    # Get the user's username and password using 'input'.
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # Set up the ChaCha generator with the user's seed.

    seed_value = syncseed_generator.get_expected_seed_value(seed)

    # Prepare the message to be sent to the server in the format 'username/password/seed_value'.
    message = f"{username}/{password}/{seed_value}"

    # Connect to the server and send the message.
    connect_to_server(message, seed_value)

# Call to main function.
if __name__ == '__main__':
    syncseed_generator = syncseed.SyncseedGenerator()
    main()
