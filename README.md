# Synchronized Seed Authentication Proof of Concept - Demo Version 1.0

## Overview

This repository contains a proof-of-concept implementation of a synchronized seed authentication system. The system demonstrates a basic method of authentication using synchronized seeds and is meant for educational purposes. It is important to note that this is not intended for use in production environments.

## How It Works

The authentication system follows a simple challenge-response mechanism:

1. **Server-side:**
   - Reads user information and seed data from external files.
   - Waits for a client connection, and extracts a username, password, and seed value from the client's initial message.
   - Verifies the client's response based on the provided credentials and the synchronized seed value.
   - Increments the seed counter server-side if authentication is successful.

2. **Client-side:**
   - Reads the synchronized seed and increment from an external file.
   - Generates a response to the server's challenge using a random seed, increment, and other parameters.
   - Communicates with the server, and if the response is verified successfully, increments the synchronized seed counter and updates the external file.

## Disclaimer

This proof of concept is solely intended to showcase the basic principles of synchronized seed authentication. It should not be considered a secure implementation and is not suitable for use in production builds. The following factors should be considered:

- **Security:** The use of the `random` module for cryptographic purposes may introduce security vulnerabilities. Consider using dedicated cryptographic libraries (e.g., `secrets`) for secure random number generation.

- **File Operations:** Storing seed and increment values in plaintext files may pose security risks. In production, secure storage mechanisms should be employed.

- **Error Handling:** The code lacks error handling, which is crucial in production environments.

- **Communication Security:** The code uses a simple socket connection for communication. In a production system, use a secure communication protocol to protect data in transit.

- **Validation of User Input:** The code takes user input for the username and password without validation or sanitation. A production system should implement proper input validation and potentially use secure password hashing.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/synchronized-seed-authentication.git
   cd synchronized-seed-authentication
   ```

2. Run the server in the Source directory:

   ```bash
   cd Source
   python main.py
   ```

3. Run one of the authentication programs included in either user directories (passwords are included in Users.txt):

   ```bash
   cd User1_Dir
   python auth.py
   ```

Follow the on-screen prompts to enter a username and password. The client will communicate with the server, and the server's response will be displayed.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements or additional features.
