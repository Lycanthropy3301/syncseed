# Changelog

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
    - Added a KeyboardInterrupt handler to shut down the server when interrupted with Ctrl+C. This ensures proper cleanup before exiting.

11. **Timeout Consideration:**
    - Implemented a timeout for connections to prevent potential issues with hanging connections.

### Notes:

- This version represents a significant improvement in code structure, error handling, and security measures. It is recommended for use over the previous version.

- Always consider security best practices and potential issues when developing or deploying a production system.
