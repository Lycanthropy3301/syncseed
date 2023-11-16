import timeit

# Import your syncSeedGenerator class
from syncseed import syncSeedGenerator

def benchmark_sync_seed_generator():
    # Create an instance of the syncSeedGenerator
    generator = syncSeedGenerator()

    # Set any parameters you want to test
    generator.set_seed_length(18)
    generator.set_challenge_rounds(100)
    generator.set_scramble_rounds(0)
    generator.set_seed_value_lower_bound(100_000_000_000)
    generator.set_seed_value_upper_bound(999_999_999_999)
    generator.set_cha_cha_generator_rounds(20)

    # Generate a seed for the generator
    seed = generator.generate_seeds(1)[0]

    generator.get_expected_seed_value(seed)

    # Use timeit to measure the time it takes to perform authentication
    time_taken = timeit.timeit(
        stmt=lambda: generator.update_seed(),
        number=1000  # You can adjust the number of iterations
    )

    print(f'Time taken for 1000 iterations: {round(time_taken, 5)} seconds')

if __name__ == '__main__':
    benchmark_sync_seed_generator()
