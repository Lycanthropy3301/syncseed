import numpy as np
import secrets
from randomgen import ChaCha

class syncSeedGenerator:

    CHALLENGE_ROUNDS = 8
    SEED_VALUE_LOWER_BOUND = 100_000_000_000
    SEED_VALUE_UPPER_BOUND = 999_999_999_999
    SEED_LENGTH = 18
    CHA_CHA_GENERATOR_ROUNDS = 20
    SCRAMBLE_ROUNDS = 0

    def __init__(self):
        self.new_seed = None

    def authenticated(self, seed_value, user_seed=None, update_auto=False):
        expected_seed_value = self.get_expected_seed_value(user_seed)
        if seed_value == expected_seed_value:
            if update_auto:
                self.update_seed()
            return True
        return False

    def update_seed(self):
        self.new_seed = self.generator.integers(10 ** (self.SEED_LENGTH - 1), 10 ** self.SEED_LENGTH)
        for _ in range(self.SCRAMBLE_ROUNDS + 1):
            self.generator = np.random.Generator(ChaCha(seed=self.new_seed, rounds=self.CHA_CHA_GENERATOR_ROUNDS))
            self.new_seed = self.generator.integers(10 ** (self.SEED_LENGTH - 1), 10 ** self.SEED_LENGTH)
        return self.new_seed

    def get_expected_seed_value(self, seed):
        self.generator = np.random.Generator(ChaCha(seed=seed, rounds=self.CHA_CHA_GENERATOR_ROUNDS))
        return ''.join(str(self.generator.integers(self.SEED_VALUE_LOWER_BOUND, self.SEED_VALUE_UPPER_BOUND, endpoint=True)) for _ in range(self.CHALLENGE_ROUNDS))

    def generate_seeds(self, n):
        return [secrets.SystemRandom().randrange(10 ** (self.SEED_LENGTH - 1), 10 ** self.SEED_LENGTH) for _ in range(n)]

    def set_seed_length(self, length):
        self.SEED_LENGTH = min(length, 18)

    def set_challenge_rounds(self, rounds):
        self.CHALLENGE_ROUNDS = rounds

    def set_scramble_rounds(self, rounds):
        self.SCRAMBLE_ROUNDS = rounds

    def set_seed_value_lower_bound(self, lower_bound):
        self.SEED_VALUE_LOWER_BOUND = lower_bound

    def set_seed_value_upper_bound(self, upper_bound):
        self.SEED_VALUE_UPPER_BOUND = upper_bound

    def set_cha_cha_generator_rounds(self, rounds):
        self.CHA_CHA_GENERATOR_ROUNDS = rounds

    def get_seed_length(self):
        return self.SEED_LENGTH

    def get_challenge_rounds(self):
        return self.CHALLENGE_ROUNDS

    def get_scramble_rounds(self):
        return self.SCRAMBLE_ROUNDS

    def get_seed_value_lower_bound(self):
        return self.SEED_VALUE_LOWER_BOUND

    def get_seed_value_upper_bound(self):
        return self.SEED_VALUE_UPPER_BOUND

    def get_cha_cha_generator_rounds(self):
        return self.CHA_CHA_GENERATOR_ROUNDS

    def get_current_seed(self):
        return self.new_seed
