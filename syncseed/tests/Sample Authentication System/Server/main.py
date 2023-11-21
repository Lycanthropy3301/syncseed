# Import the required libraries.
import syncseed.syncseed as syncseed
import socket
import logging
import threading

# Import and unpack the config file
with open('..\\Config\\options.cfg') as config_file:
    config_options = {key[0].strip(): value.strip() for line in config_file if (key := line.split('=', 1)) and '[' not in key[0] and key[0].strip() for value in key}

# Unpack the Seed_Value challenge upper and lower bounds and number of challenge rounds. These must be consistent with both the server and client.
SEED_VALUE_LOWER_BOUND = int(config_options['SEED_VALUE_LOWER_BOUND'])
SEED_VALUE_UPPER_BOUND = int(config_options['SEED_VALUE_UPPER_BOUND'])
SEED_LENGTH = int(config_options['SEED_LENGTH'])
CHALLENGE_ROUNDS = int(config_options['CHALLENGE_ROUNDS'])

# Declare standard server responses.
AUTH_SUCCESS = config_options['AUTH_SUCCESS']
AUTH_FAIL = config_options['AUTH_FAIL']

# Set up a basic logging system.
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')

# Loading Users and Seeds from a file. You can load these from a database instead for a production system.
with open("Users.txt", 'r') as user_file:
    users = user_file.read().split('\n')

with open("Seeds.txt", 'r') as seed_file:
    seeds = seed_file.read().split('\n')
    seeds.pop(-1)

# Dictionary comprehensions to intialise dictionaries to hold username and passwords as well as seed values tied to each username.
user_password = {user.split(' ')[0]: user.split(' ')[1] for user in users}
seed_users = {seed.split(' ')[0]: int(seed.split(' ')[1]) for seed in seeds}



# Function to check if a user succesfully authenticates. Returns a boolean at all times, even when an error is encountered.
def authenticated(user, password, seed_value):

    # Basic exception handling. Catches KeyErrors and ValueErrors as seen later in the code.
    try:






        # Check if user-transmitted seed_value is actually an integer, return false otherwise.
        if not(seed_value.isnumeric()):
            return False

        # Set up the ChaCha generator with the user's seed.
        generator = np.random.Generator(ChaCha(seed=seed, rounds=20))

        seed_message = ''

        # Generate a large random number based on the value of CHALLENGE_ROUNDS
        for i in range(CHALLENGE_ROUNDS):
            generated_seed_value = generator.integers(SEED_VALUE_LOWER_BOUND, SEED_VALUE_UPPER_BOUND, endpoint=True)
            seed_message += str(generated_seed_value)

        # Check if seed_values mach
        if seed_value == seed_message:
            generator = np.random.Generator(ChaCha(seed=generated_seed_value, rounds=20))
            new_seed = generator.integers(10**(SEED_LENGTH-1), (10**SEED_LENGTH)-1, endpoint=True)
            seed_users[user] = new_seed
            return True

        # Return false if seed value doesn't match.
        return False

    # Exception handling as aforementioned.
    except (KeyError, ValueError) as exception:
        logging.error(f"Error during authentication for {user}: {str(exception)}")

def handle_connection(client):

    # Basic exception handling. Catches errors and logs them.
    # Checks of format, username and password use guard clause structure.
    try:

        # Set the client timeout to 10 seconds.
        client.settimeout(10)

        # Receives a message from the user.
        message = client.recv(512).decode()

        # Checks if the message follows the 'username/password/seed_value' format. Trasmits 'Failed' and closes the connection if otherwise.
        if len(message.split('/')) != 3:
            client.send(AUTH_FAIL.encode())
            client.close()
            return

        # Split the message into its username, password and seed_value components.
        username, password, seed_value = message.split('/')

        # Check if the transmitted username is present in the server username dictionary. Transmits 'Failed' and closes the connection if otherwise.
        if username not in user_password:
            client.send(AUTH_FAIL.encode())
            client.close()
            return

        # Check if user passwords match, return if they don't.
        if password != user_password[username]:
            return

        # Exctract Seeds from the seed_users dictionary.
        seed = seed_users[username]

        syncSeedGenerator = syncseed.syncSeedGenerator()

        # Call to the syncseed authentication function
        if syncSeedGenerator.authenticated(seed_value, seed):

            new_seed = syncSeedGenerator.update_seed()

            seed_users[username] = new_seed

            # If 'authenticated' returns True (the user is authenticated), then Transmit 'Success!'.
            client.send(AUTH_SUCCESS.encode())

            # Open and clear the 'Seeds.txt' File. In a production system this would simply update the seed database.
            with open("Seeds.txt", 'w') as seed_file:
                seed_file.write('')

            # Iterate over key value pairs of the server seed dictionary.
            for key, value in seed_users.items():

                # Re-write the contents of the server seed dictionary to 'Seeds.txt'.
                with open("Seeds.txt", 'a') as seed_file:
                    seed_file.write(f'{key} {value}\n')

            # logs the authentication when a user is authenticated.
            logging.info(f'{username} has authenticated!')

            # Finally, closes the connection.
            client.close()

        else:

            # If 'authenticated' returns False (the user is not authenticated), then transmit 'Failed' to the client and close it's connection.
            client.send(AUTH_FAIL.encode())
            client.close()
            return

    # Exception handling as aforementioned.
    except socket.timeout:
        logging.warning("Connection timed out.")
        client.send(AUTH_FAIL.encode())

    except Exception as exception:
        logging.error(f"Unexpected error: {str(exception)}")

    # Close the client connection at the end.
    finally:
        client.close()

# Mainloop.
def main():
    logging.info("Server started.")

    # Start the server socket. Binds to port 450.
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(('', 450))
    listener.listen(4)

    # Set a timeout on the server socket
    listener.settimeout(0.5)

    # Begin the mainloop.
    while True:

        # Basic exception handling. Catches errors and logs them.
        try:
            # Accept a users connection. Since the return value of socket.socket.accept() is a tuple, these values are extracted into the client object and the client's address.
            try:
                client, address = listener.accept()

            # Handling Ctrl+C.
            except KeyboardInterrupt:
                logging.info("Server shutting down.")
                break

            # Start a thread that handles the clients connection
            threading.Thread(target=handle_connection, args=(client,)).start()

        # Continue as normal if socket times out.
        except socket.timeout:
            pass

        # Handling Ctrl+C.
        except KeyboardInterrupt:
            logging.info("Server shutting down.")
            break

        # Exception handling as aforementioned.
        except Exception as exception:
            logging.error(f"Unexpected error: {str(exception)}")

    # Close the server socket if loop is exited.
    listener.close()

# Run the mainloop function.
if __name__ == '__main__':
    main()
