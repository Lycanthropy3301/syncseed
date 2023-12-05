# Changelog

# Major Update: Syncseed - Version 1.1.0

## New features

1. **SEA (Syncseed Exchange Algorithm):**
	 - Introduced an additional module called `seed_exchange` containing SEA.
	 - Provides three methods of securely creating or exchanging seeds using a Trusted Authority (TU).

2. **Bug Fixes:**
	 - Fixed a critical bug which caused the `mutate_seed` function to fail.

3. **Seed Exchange Example:**
	- Added an example of the SEA algorithm in the Syncseed tests folder.

4. **Documentation:**
	- Added additional documentation relating to SEA.

4. **SEA Benchmark:**
	- Added a customizable benchmarking tool for SEA.

### Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements or additional features.

# Syncseed - Version 1.0.1

## New features

1. **Test Code Improvements:**
   - Streamlined and removed redundant code.

2. **Syncseed Properties:**
   - Implementation of properties for more intuitive configuration adjustments.
   - Proper handling for invalid assignments to configuration options.

3. **Benchmark Documentation**
   - Added documentation for `cycle_generation_test.py` and `benchmark.py`.

4. **Bug Fixes:**
   - Fixed a bug which caused the sample authentication system to fail to execute.
   - Fixed a bug where the sample authentication system would not load it's configuration properly.

### Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements or additional features.

# Syncseed - Version 1.0.0

## New Features

1. **Synchronized Seed System:**
   - Syncseed transitions from the old seed-increment system to a dynamic seed system.
   - Synchronized seeds dynamically change with each authentication attempt, enhancing security against various attacks.

2. **Configurability:**
   - Fine-tune key parameters for a tailored balance between security and performance.
   - Adjust seed length, challenge rounds, scramble rounds, and other settings to match specific application requirements.

3. **Update Seed Functionality:**
   - Introduces the "update seed" function, allowing periodic refreshing of seed values to maintain long-term security.
   - Introduces seed mutations, enhancing the unpredictability of the overall system.

5. **User-Friendly API:**
   - Provides a straightforward API for easy integration into Python applications.

## Configuration Options

1. `set_seed_length(length)`: Set the length of the synchronized seed.
2. `set_challenge_rounds(rounds)`: Define the number of challenge rounds for enhanced security.
3. `set_scramble_rounds(rounds)`: Configure the scramble rounds to balance security and performance.
4. `set_seed_value_lower_bound(lower_bound)`: Set the lower bound for seed values.
5. `set_seed_value_upper_bound(upper_bound)`: Set the upper bound for seed values.
6. `set_cha_cha_generator_rounds(rounds)`: Adjust the number of ChaCha generator rounds.

### Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements or additional features.


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


# Synchronized Seed Authentication Proof of Concept - Version 1.1

## Changes:

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

## Notes:

- This version represents a significant improvement in code structure, error handling, and security measures. It is recommended for use over the previous version.

- Always consider security best practices and potential issues when developing or deploying a production system.
