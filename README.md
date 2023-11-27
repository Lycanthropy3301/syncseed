# Syncseed - Authentication Module

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Getting Started](#getting-started)
4. [Additional Notes](#additional-notes)
6. [Configuration](#configuration)
7. [Performance Optimization](#performance-optimization)
8. [Acknowledgments](#acknowledgments)
9. [License](#license)
10. [Author](#author)


## Overview

Syncseed has evolved from a standalone proof of concept into a robust authentication module designed to enhance security in Python applications. This module leverages a synchronized seed-based challenge-response system to verify user authenticity. Seeds are generated using a CSPRNG to ensure unpredictability.

## Key Features

- **Synchronized Seeds:** The core of Syncseed lies in synchronized seeds that dynamically change with each authentication attempt. These seeds are initialized when a user signs up and are never transmitted after the initial sign-up operation.
- **Configurability:** Adjust key parameters such as seed length, challenge rounds, and scramble rounds to balance security and performance based on specific application needs.
- **ChaCha PRNG:** Utilizes the ChaCha pseudo-random number generator for generating secure and unpredictable seed values.
- **User-Friendly API:** The module offers a straightforward API for integration into existing Python applications.


## Getting Started

To integrate Syncseed into your project, follow these steps:

### 1. Installation:
   ```bash
   pip install syncseed
   ```

### 2. Usage:

**Server-Side:**

```python
# Initialize Syncseed
from syncseed.syncseed import SyncseedGenerator
sync_seed = SyncseedGenerator()

# Authenticate a user
if sync_seed.authenticated(user_seed, seed_value):
    # Update the seed
    new_seed = sync_seed.update_seed()
    print("Authentication successful!")
else:
    print("Authentication failed.")
```

**Client-Side:**

```python
# Initialize Syncseed
from syncseed.syncseed import SyncseedGenerator
sync_seed = SyncseedGenerator()

# [Load syncseed configuration to match that of the server...]
# Assume 'user_seed' is the user's seed value stored in a file or database
user_seed = 123456789

# Generate the challenge value to transmit
seed_value = sync_seed.get_expected_seed_value(user_seed)
```

## Additional Notes

### Seed Mutation for Enhanced Security

In addition to the core authentication process, Syncseed provides a mechanism to further fortify its resistance against brute force attacks. Periodically mutating the seed adds an extra layer of security, making it more challenging for malicious actors to compromise user credentials.

#### Why Seed Mutation?

The purpose of seed mutation is to disrupt any attempt to systematically guess or iterate through possible seed combinations. By periodically mutating the seed, third parties are thwarted in their efforts to exploit a compromised client seed.

#### Integration into Production Systems

In a production environment, consider incorporating the `mutate_seed` function provided by Syncseed into your application's workflow. This function initiates a mutation on the current seed value, producing a new seed that can be used in subsequent authentication attempts.

Here's an example of how you might use the `mutate_seed` function:

```python
import syncseed.syncseed as syncseed

# Initialize the syncseed generator
sync_seed = syncseed.SyncseedGenerator()

# Assume 'current_seed' is the current seed value you want to mutate
current_seed = 123456789

# Call the 'mutate_seed' function to perform a mutation on the seed
mutated_seed = sync_seed.mutate_seed(current_seed)

# Now 'mutated_seed' contains the result of the mutation
print(f'Mutated Seed: {mutated_seed}')
```

Integrating seed mutation into your application's security strategy enhances the robustness of Syncseed, contributing to a more secure authentication mechanism.

## Configuration

Fine-tune Syncseed for your application by adjusting configuration parameters:

- `set_seed_length(length)`: Set the length of the synchronized seed.
- `set_challenge_rounds(rounds)`: Define the number of challenge rounds for enhanced security.
- `set_scramble_rounds(rounds)`: Configure the scramble rounds to balance security and performance.
- `set_seed_value_lower_bound(lower_bound)`: Set the lower bound for seed values.
- `set_seed_value_upper_bound(upper_bound)`: Set the upper bound for seed values.
- `set_cha_cha_generator_rounds(rounds)`: Adjust the number of ChaCha generator rounds.

For a more in-depth guide for deploying syncseed, refer to the 'Syncseed Deployment Guide' on my [github](https://github.com/Lycanthropy3301/syncseed)

## Performance Optimization

Syncseed offers flexibility to optimize performance based on specific requirements. Regularly test and analyze the execution time under different configurations to strike an optimal balance between security and performance. Within the 'tests' folder of the project, you'll find a performance benchmarking program for Syncseed. Feel free to customize this program to evaluate various configurations. Additionally, the algorithm's security can be assessed using the cycle generation test, also available in the same folder. This test allows you to determine the number of unique seeds that Syncseed can generate before a cycle forms with seed values.

## Acknowledgments

Syncseed is a collaborative effort, benefitting from community feedback and contributions. Your insights and suggestions are highly valued in the continued improvement of this authentication module. Feel free to raise issues, propose enhancements, or contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Author

[Kavin Muthuselvan](https://github.com/Lycanthropy3301)
