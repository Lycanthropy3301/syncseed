import numpy as np
import secrets
from randomgen import ChaCha

class SyncseedGenerator:

    CHALLENGE_ROUNDS = 8
    SEED_VALUE_LOWER_BOUND = 100_000_000_000
    SEED_VALUE_UPPER_BOUND = 999_999_999_999
    SEED_LENGTH = 18
    CHA_CHA_GENERATOR_ROUNDS = 20
    SCRAMBLE_ROUNDS = 0
    MUTATE_SEED = True

    def __init__(self):
        self.new_seed = None
        self.generator = np.random.Generator(ChaCha(seed=self.new_seed, rounds=self.CHA_CHA_GENERATOR_ROUNDS))

    def authenticated(self, seed_value: int, user_seed: int = 0, update_auto: bool = False) -> bool:
        """Check if a user is authenticated.

        Args:
            seed_value (str): The string the user transmits in response to the server challenge.
            user_seed (int): The user's seed stored server-side. Defaults to '0'.
            update_auto (bool): Whether to automatically update the user's seed.

        Returns:
            bool: True if authentication is succesful, False otherwise.
        """
        expected_seed_value = self.get_expected_seed_value(user_seed)
        if seed_value == expected_seed_value:
            if update_auto:
                self.update_seed()
            return True
        return False

    def update_seed(self) -> int:
        """Update the internatlly stored seed, and return it.

        Returns:
            int: updated seed value
        """
        self.new_seed = self.generator.integers(10 ** (self.SEED_LENGTH - 1), 10 ** self.SEED_LENGTH)
        for _ in range(self.SCRAMBLE_ROUNDS+1):
            self.generator = np.random.Generator(ChaCha(seed=self.new_seed, rounds=self.CHA_CHA_GENERATOR_ROUNDS))
            self.new_seed = self.generator.integers(10 ** (self.SEED_LENGTH - 1), 10 ** self.SEED_LENGTH)

        return self.new_seed

    def mutate_seed(self, seed: int) -> int:
        """Mutate the seed passed as an argument, and return it.

        Args:
            seed (int): The seed to be mutated.

        Returns:
            int: mutated seed value
        """
        xor_value = self.generator.integers(1, 2**63)
        seed ^= xor_value
        self.generator = np.random.Generator(ChaCha(seed=seed, rounds=self.CHA_CHA_GENERATOR_ROUNDS))
        self.generator.jump(self.generator.integers(1,6))
        self.new_seed = self.generator.integers(10 ** (self.SEED_LENGTH - 1), 10 ** self.SEED_LENGTH)

        return self.new_seed

    def get_expected_seed_value(self, seed: int) -> str:
        """Return the challenge response expected by the server for the client's seed.

        Args:
            seed (int): The client's seed.

        Returns:
            str: The value expected as a response.
        """
        self.generator = np.random.Generator(ChaCha(seed=seed, rounds=self.CHA_CHA_GENERATOR_ROUNDS))
        return ''.join(str(self.generator.integers(self.SEED_VALUE_LOWER_BOUND, self.SEED_VALUE_UPPER_BOUND, endpoint=True)) for _ in range(self.CHALLENGE_ROUNDS))

    def generate_seeds(self, n: int) -> list:
        """Generate a list random seeds to distribute to new users.

        Args:
            n (int): The number of seeds to generate.

        Returns:
            list: The generated seeds.
        """
        return [secrets.SystemRandom().randrange(10 ** (self.SEED_LENGTH - 1), 10 ** self.SEED_LENGTH) for _ in range(n)]

    def set_seed_length(self, length: int):
        self.SEED_LENGTH = min(length, 18)

    def set_challenge_rounds(self, rounds: int):
        self.CHALLENGE_ROUNDS = rounds

    def set_scramble_rounds(self, rounds: int):
        self.SCRAMBLE_ROUNDS = rounds

    def set_seed_value_lower_bound(self, lower_bound: int):
        self.SEED_VALUE_LOWER_BOUND = lower_bound

    def set_seed_value_upper_bound(self, upper_bound: int):
        self.SEED_VALUE_UPPER_BOUND = upper_bound

    def set_cha_cha_generator_rounds(self, rounds: int):
        self.CHA_CHA_GENERATOR_ROUNDS = rounds

    def get_seed_length(self) -> int:
        return self.SEED_LENGTH

    def get_challenge_rounds(self) -> int:
        return self.CHALLENGE_ROUNDS

    def get_scramble_rounds(self) -> int:
        return self.SCRAMBLE_ROUNDS

    def get_seed_value_lower_bound(self) -> int:
        return self.SEED_VALUE_LOWER_BOUND

    def get_seed_value_upper_bound(self) -> int:
        return self.SEED_VALUE_UPPER_BOUND

    def get_cha_cha_generator_rounds(self) -> int:
        return self.CHA_CHA_GENERATOR_ROUNDS

    def get_current_seed(self) -> int:
        """Return the LASTEST updated seed value stored in the syncseed generator"""
        return self.new_seed
