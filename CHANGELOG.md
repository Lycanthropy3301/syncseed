# Changelog

# Synchronized Seed Authentication Proof of Concept - Version 1.2

## Changes

1. **Configuration File Integration:**
   - Added support for configuration files to centralize and manage server settings.
   - Introduced a configuration file (`options.cfg`) for easy adjustment of parameters, including seed value bounds, challenge rounds, and server responses.

2. **Dynamic Seed Challenge Rounds:**
   - Implemented dynamic challenge rounds in the authentication process.
   - Challenge rounds enhance security by introducing variability and unpredictability during user authentication.

3. **Improved Logging:**
   - Enhanced the logging system to capture more detailed information.
   - Log entries now include timestamps, log levels, and specific details about authentication errors.

4. **Timeout Handling:**
   - Implemented timeout handling for server socket connections to improve responsiveness.
   - The server now gracefully handles timeouts, logging a warning and transmitting an authentication failure response.

5. **Code Refactoring and Cleanup:**
   - Refactored code to improve readability and maintainability.
   - Removed redundant code, improved variable naming, and organized imports for a cleaner codebase.

6. **Directory Structure Update:**
   - Adjusted the directory structure for improved organization.
   - Configuration files are now stored in a dedicated `Config` directory.

7. **Bug Fixes:**
   - Addressed an issue with Ctrl+C interrupt handling during socket acceptance.
   - Improved server shutdown behavior for a more reliable user experience.

8. **Documentation Update:**
   - Updated the README.md file to reflect the changes in configuration, usage, and contribution guidelines.
   - Included a brief overview of the ChaCha algorithm and the role of challenge rounds in the authentication process.

10. **Overall System Enhancement:**
    - Improved the overall system by combining cryptographic best practices with configuration flexibility for educational and experimental use.

## Important Notes

- **Configuration File (`options.cfg`):**
  - Users are encouraged to review and customize the configuration file to meet specific requirements.
  - Ensure consistent configuration between server and client components for successful authentication.
  - Run configurator.py in the 'Config' folder to update the config file and reconfigure seeds.

- **Educational Purpose:**
  - This proof of concept remains designed for educational purposes and is not intended for production use.
  - Considerations for production environments, including secure storage mechanisms and communication protocols, should be addressed.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements or additional features.


## Version 1.1

### Changes:

1. **Enhanced Error Handling:**
   - Added proper error handling mechanisms throughout the code to catch and log exceptions. This provides better insight into potential issues.

2. **Logging Implementation:**
   - Replaced print statements with the `logging` module for more structured and configurable logging. Now, error messages and important events are logged.

3. **Code Comments:**
   - Added comments to explain the purpose and functionality of specific code blocks. Improved code readability and understanding.

4. **Separation of Concerns:**
   - Introduced smaller functions to break down the `main` function into more manageable components.

6. **Security Measures:**
   - Replaced the use of plain-text passwords with secure password hashing in a real-world scenario. Additionally, introduced the concept of encrypting communication using a secure protocol like TLS/SSL.

7. **Response Constants:**
   - Defined constants for server response messages (`'Failed!'`, `'Success!'`) to improve code maintainability and consistency.

8. **Random Number Generation:**
   - Swapped the use of `random.randint` with the ChaCha CSPRNG from the `randomgen` library. This enhances the security of random number generation in the authentication process.

9. **Concurrent Handling:**
   - Introduced a basic mechanism for handling multiple simultaneous connections using threading. This lays the foundation for improved concurrency as the system scales.

10. **CTRL+C Shutdown:**
    - Added a KeyboardInterrupt handler to gracefully shut down the server when interrupted with Ctrl+C. This ensures proper cleanup before exiting.

11. **Timeout Consideration:**
    - Implemented a timeout for connections to prevent potential issues with hanging connections.

### Notes:

- This version represents a significant improvement in code structure, error handling, and security measures. It is recommended for use over the previous version.

- Always consider security best practices and potential issues when developing or deploying a production system.
