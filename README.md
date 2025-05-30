> :warning: Syncseed is no longer maintained!
> Although not proven insecure, insufficient research has been conducted in order to verify its viability
> However, you are still welcome to use and treat the project as a proof-of-concept
> Use at your own risk! The owner retains no responsibility of damages as a result of use of this module

# Syncseed - Authentication Module

## Table of Contents

1. [Overview](#overview)
2. [New Features](#new-features)
3. [Key Features](#key-features)
4. [Getting Started](#getting-started)
5. [Additional Notes](#additional-notes)
6. [Configuration](#configuration)
7. [Performance Optimization](#performance-optimization)
8. [Acknowledgments](#acknowledgments)
9. [License](#license)
10. [Author](#author)

## Overview

Syncseed is an authentication module that leverages a synchronized seed-based challenge-response system to verify user authenticity. Seeds are generated using a CSPRNG to ensure unpredictability. Now, Syncseed also contains a seed exchange system, which can be used in peer-to-peer communication system through an intermediate Trusted Authority (TA).

## Major Update - New Features
The Syncseed algorithm now contains an additional module - `seed_exchange`. This module contains three variations of a solution for dynamic peer to peer authentication using Syncseed, made possible through the Syncseed Exchange Algorithm (SEA). Please refer to the readme under `syncseed/tests/Seed Exchange Example` for more information.

## Key Features

- **Synchronized Seeds:** The core of Syncseed lies in synchronized seeds that dynamically change with each authentication attempt. These seeds are initialized when a user signs up and are never transmitted after the initial sign-up operation.
- **Configurability:** Adjust key parameters such as seed length, challenge rounds, and scramble rounds to balance security and performance based on specific application needs. Also fine tune the seed exchange module using the parameters seed length and transform rounds
- **ChaCha PRNG:** Utilizes the ChaCha pseudo-random number generator for generating secure and unpredictable seed values.
- **User-Friendly API:** The module offers straightforward APIs for integration into existing Python applications.


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
gen = SyncseedGenerator()

# Authenticate a user
if gen.authenticated(user_seed, seed_value):
    # Update the seed
    new_seed = gen.update_seed()
    print("Authentication successful!")
else:
    print("Authentication failed.")
```

**Client-Side:**

```python
# Initialize Syncseed
from syncseed.syncseed import SyncseedGenerator
gen = SyncseedGenerator()

# [Load syncseed configuration to match that of the server...]
# Assume 'user_seed' is the user's seed value stored in a file or database
user_seed = 123456789

# Generate the challenge value to transmit
seed_value = gen.get_expected_seed_value(user_seed)
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
gen = syncseed.SyncseedGenerator()

# Assume 'current_seed' is the current seed value you want to mutate
current_seed = 123456789

# Call the 'mutate_seed' function to perform a mutation on the seed
mutated_seed = gen.mutate_seed(current_seed)

# Now 'mutated_seed' contains the result of the mutation
print(f'Mutated Seed: {mutated_seed}')
```

Integrating seed mutation into your application's security strategy enhances the robustness of Syncseed, contributing to a more secure authentication mechanism.

## Configuration

Fine-tune Syncseed for your application by adjusting its various properties:

- `seed_length`: Set the length of the synchronized seed.
- `challenge_rounds`: Define the number of challenge rounds for enhanced security.
- `scramble_rounds`: Configure the scramble rounds to balance security and performance.
- `seed_value_lower_bound`: Set the lower bound for seed values.
- `seed_value_upper_bound`: Set the upper bound for seed values.
- `cha_cha_generator_rounds`: Adjust the number of ChaCha generator rounds.

For a more in-depth guide for deploying Syncseed, refer to the [Syncseed Deployment Guide](https://github.com/Lycanthropy3301/syncseed/blob/master/DeploymentGuide.md)

## Performance Optimization

Syncseed offers flexibility to optimize performance based on specific requirements. Regularly test and analyze the execution time under different configurations to strike an optimal balance between security and performance. Within the `syncseed/tests` folder of the project, you'll find a performance benchmarking program for Syncseed. Feel free to customize this program to evaluate various configurations. Additionally, the algorithm's security can be assessed using the cycle generation test, also available in the same folder. This test allows you to determine the number of unique seeds that Syncseed can generate before a cycle forms with seed values.

## Acknowledgments

Syncseed is a collaborative effort, benefitting from community feedback and contributions. Your insights and suggestions are highly valued in the continued improvement of this authentication module. Feel free to raise issues, propose enhancements, or contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Author

[Kavin Muthuselvan](https://github.com/Lycanthropy3301)

[Syncseed's Github](https://github.com/Lycanthropy3301/syncseed)
