import timeit # Requires timeit. Use: "pip install timeit"

from syncseed.syncseed import SyncseedGenerator

def benchmark_sync_seed_generator():
    generator = SyncseedGenerator()

    # Modify these as you please
    generator.set_seed_length(18)
    generator.set_challenge_rounds(100)
    generator.set_scramble_rounds(0)
    generator.set_seed_value_lower_bound(100_000_000_000)
    generator.set_seed_value_upper_bound(999_999_999_999)
    generator.set_cha_cha_generator_rounds(20)

    seed = generator.generate_seeds(1)[0]

    generator.get_expected_seed_value(seed)

    time_taken = timeit.timeit(
        stmt=lambda: generator.update_seed(),
        number=1000  # You can adjust the number of iterations
    )

    print(f'Time taken for 1000 iterations: {round(time_taken, 5)} seconds')

if __name__ == '__main__':
    benchmark_sync_seed_generator()
