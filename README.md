# SyncSeed - Authentication Module

## Overview

SyncSeed has evolved from a standalone proof of concept into a robust authentication module designed to enhance security in Python applications. This module leverages a synchronized seed-based challenge-response system to verify user authenticity.

## Key Features

- **Synchronized Seeds:** The core of SyncSeed lies in synchronized seeds that dynamically change with each authentication attempt. These seeds as initialized when a user signs up, and are never transmitted after the initial sign up operation.

- **Configurability:** Adjust key parameters such as seed length, challenge rounds, and scramble rounds to balance security and performance based on specific application needs.

- **ChaCha PRNG:** Utilizes the ChaCha pseudo-random number generator for generating secure and unpredictable seed values.

- **User-Friendly API:** The module offers a straightforward API for integration into existing Python applications.

## Getting Started

To integrate SyncSeed into your project, follow these steps:

1. **Installation:**
   ```bash
   pip install syncseed
   ```

2. **Usage:**
   ```python
   from syncseed import SyncSeedGenerator

   # Initialize SyncSeed
   sync_seed = SyncSeedGenerator()

   # Authenticate a user
   if sync_seed.authenticated(user_seed, seed_value):

        # Update the seed
        new_seed = sync_seed.update_seed()
        print("Authentication successful!")

   else:
        print("Authentication failed.")
   ```

## Configuration

Fine-tune SyncSeed for your application by adjusting configuration parameters:

- `set_seed_length(length)`: Set the length of the synchronized seed.
- `set_challenge_rounds(rounds)`: Define the number of challenge rounds for enhanced security.
- `set_scramble_rounds(rounds)`: Configure the scramble rounds to balance security and performance.
- `set_seed_value_lower_bound(lower_bound)`: Set the lower bound for seed values.
- `set_seed_value_upper_bound(upper_bound)`: Set the upper bound for seed values.
- `set_cha_cha_generator_rounds(rounds)`: Adjust the number of ChaCha generator rounds.

## Performance Optimization

SyncSeed offers flexibility to optimize performance based on specific requirements. Regularly test and analyze the execution time under different configurations to strike an optimal balance between security and performance.

## Acknowledgments

SyncSeed is a collaborative effort, benefitting from community feedback and contributions. Your insights and suggestions are highly valued in the continued improvement of this authentication module.

**Note:** SyncSeed is continuously evolving, and your feedback is crucial for its refinement. Feel free to raise issues, propose enhancements, or contribute to the project.
