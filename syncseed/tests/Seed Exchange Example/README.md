
# Syncseed Exchange Algorithm (SEA) Demo

Syncseed Exchange Algorithm (SEA) is a secure seed exchange module built on the foundation of the Syncseed authentication algorithm. This demonstration showcases the basic usage of SEA with and without the use of nonces.

There are three modes supported by the Syncseed Exchange Algorithm: Parity, Exchange and Selection. Consult the deployment guide in this repos root folder for more information.

## Getting Started

To use SEA, follow these steps:

1. **Installation:**
   - Install the `syncseed` module.

```bash
pip install syncseed
```

2. **Usage:**
   - Import the `syncseed.seed_exchange` module.
   - Initialize the Syncseed Exchange Algorithm (SEA).
   - Set the desired seed length.

```python
import syncseed.seed_exchange as seed_exchange

# Initialize the Syncseed Exchange Algorithm (SEA)
sea = seed_exchange.SyncseedExchangeAlgorithm()

# Set the seed length for demonstration purposes
sea.seed_length = 9
```

3. **Seed Exchange Without Nonce:**
   - Exchange seeds securely between two users without using nonces.

```python
# User 1 and User 2 exchange seeds securely through SEA
user1_seed = 123456789
user2_seed = 987654321

# Generate parity transformations for both users
transformation_user1, transformation_user2 = sea.parity_transformation(user1_seed, user2_seed)

# Exchange transformations securely between users
transformation_received_user1 = transformation_user2
transformation_received_user2 = transformation_user1

# Retrieve the updated seeds from the received transformations
updated_seed_user1 = sea.extract_parity(user1_seed, transformation_received_user1)
updated_seed_user2 = sea.extract_parity(user2_seed, transformation_received_user2)

# Print the updated seeds without nonces.
print("Without Nonce:")
print(f"Updated Seed for User 1: {updated_seed_user1}")
print(f"Updated Seed for User 2: {updated_seed_user2}")
```

4. **Seed Exchange With Nonces:**
   - Generate nonces for both users.
   - Exchange seeds securely between two users using nonces and additional transformation rounds.

```python
import secrets

# Generate nonces for both users
nonce_user1 = secrets.SystemRandom().randrange(2**31)
nonce_user2 = secrets.SystemRandom().randrange(2**31)

# Generate exchange transformations for both users with nonces
transformation_user1, transformation_user2 = sea.exchange_transformation(user1_seed, user2_seed, nonce_user1, nonce_user2)

# Exchange transformations securely between users
transformation_received_user1 = transformation_user2
transformation_received_user2 = transformation_user1

# Retrieve the updated seeds from the received transformations with nonces
updated_seed_user1 = sea.extract_exchange(user1_seed, transformation_received_user1, nonce_user1)
updated_seed_user2 = sea.extract_exchange(user2_seed, transformation_received_user2, nonce_user2)

# Print the updated seeds with nonces.
print(f"Updated Seed for User 1: {updated_seed_user1}")
print(f"Updated Seed for User 2: {updated_seed_user2}")
```

5. **Adjusting Transformation Rounds:**
   - Optionally, you can adjust the number of transformation rounds.
   - Nonces are also optional.

```python
# Adjust the number of transformation rounds
sea.transform_rounds = 8
```

## Note
This is a basic demonstration of SEA. For production scenarios, ensure the secure exchange of nonces and transformations through a trusted communication channel.
