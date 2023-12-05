import syncseed.seed_exchange as seed_exchange
import secrets

# Initialize the Syncseed Exchange Algorithm (SEA)
sea = seed_exchange.SyncseedExchangeAlgorithm()

# Set the seed length for demonstration purposes
sea.seed_length = 9

# User 1 and User 2 exchange seeds securely through SEA
user1_seed = 123456789
user2_seed = 987654321

# Generate parity transformations for both users
transformation_user1, transformation_user2 = sea.parity_transformation(user1_seed, user2_seed)

# Exchange transformations securely between users
# In a real scenario, this exchange would happen through a secure channel
# For simplicity, we directly assign the transformations here
transformation_received_user1 = transformation_user2
transformation_received_user2 = transformation_user1

# Retrieve the updated seeds from the received transformations
updated_seed_user1 = sea.extract_parity(user1_seed, transformation_received_user1)
updated_seed_user2 = sea.extract_parity(user2_seed, transformation_received_user2)

# Print the updated seeds
print("\nWithout Nonce:")
print(f"Updated Seed for User 1: {updated_seed_user1}")
print(f"Updated Seed for User 2: {updated_seed_user2}\n")

sea.transform_rounds = 8

# Generate nonces for both users
nonce_user1 = secrets.SystemRandom().randrange(2**31)
nonce_user2 = secrets.SystemRandom().randrange(2**31)

# Generate selection transformations for both users with nonces
transformation_user1, transformation_user2 = sea.selection_transformation(user1_seed, user2_seed, nonce_user1, nonce_user2)

# Exchange transformations securely between users
transformation_received_user1 = transformation_user1
transformation_received_user2 = transformation_user2

# Retrieve the updated seeds from the received transformations with nonces
updated_seed_user1 = sea.extract_selection(user1_seed, transformation_received_user1, nonce_user1)
updated_seed_user2 = sea.extract_selection(user2_seed, transformation_received_user2, nonce_user2)

# Print the updated seeds
print("With Nonce and transformation rounds:")
print(f"Updated Seed for User 1: {updated_seed_user1}")
print(f"Updated Seed for User 2: {updated_seed_user2}\n")
