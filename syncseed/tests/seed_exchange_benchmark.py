import timeit
import secrets
import syncseed.seed_exchange as seed_exchange

sea = seed_exchange.SyncseedExchangeAlgorithm()

# Modify these as you please
sea.seed_length = 18
sea.transform_rounds = 0

user1_seed = 123456789123456789
user2_seed = 987654321987654321

iterations = 1000

print(f'--Result for {iterations} iterations--')

# Benchmark Parity Transformation
parity_time = timeit.timeit(lambda: sea.parity_transformation(user1_seed, user2_seed), number=iterations)
print(f"Parity Transformation Time: {parity_time:.6f} seconds")

# Benchmark Exchange Transformation
exchange_time = timeit.timeit(lambda: sea.exchange_transformation(user1_seed, user2_seed), number=iterations)
print(f"Exchange Transformation Time: {exchange_time:.6f} seconds")

# Benchmark Selection Transformation
selection_time = timeit.timeit(lambda: sea.selection_transformation(user1_seed, user2_seed), number=iterations)
print(f"Selection Transformation Time: {selection_time:.6f} seconds")
