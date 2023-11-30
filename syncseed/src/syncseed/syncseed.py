import numpy as np
import secrets
from randomgen import ChaCha

class SyncseedGenerator():

    def __init__(self):
        self.__new_seed = 0
        self.seed_length = 18
        self.challenge_rounds = 8
        self.seed_value_lower_bound = 100_000_000_000
        self.seed_value_upper_bound = 999_999_999_999
        self.cha_cha_generator_rounds = 20
        self.scramble_rounds = 0
        self.generator = np.random.Generator(ChaCha(seed=self.__new_seed, rounds=20))

    def authenticated(self, seed_value: str, user_seed: int = 0, update_auto: bool = False) -> bool:
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
        self.__new_seed = self.generator.integers(10 ** (self.seed_length - 1), 10 ** self.seed_length)
        for _ in range(self.scramble_rounds+1):
            self.generator = np.random.Generator(ChaCha(seed=self.__new_seed, rounds=self.cha_cha_generator_rounds))
            self.__new_seed = self.generator.integers(10 ** (self.seed_length - 1), 10 ** self.seed_length)

        return self.__new_seed

    def mutate_seed(self, seed: int) -> int:
        """Mutate the seed passed as an argument, and return it.

        Args:
            seed (int): The seed to be mutated.

        Returns:
            int: mutated seed value
        """
        xor_value = self.generator.integers(1, 2**63)
        seed ^= xor_value
        self.generator = np.random.Generator(ChaCha(seed=seed, rounds=self.cha_cha_generator_rounds))
        self.generator.jump(self.generator.integers(1,6))
        self.__new_seed = self.generator.integers(10 ** (self.seed_length - 1), 10 ** self.seed_length)

        return self.__new_seed

    def get_expected_seed_value(self, seed: int) -> str:
        """Return the challenge response expected by the server for the client's seed.

        Args:
            seed (int): The client's seed.

        Returns:
            str: The value expected as a response.
        """
        self.generator = np.random.Generator(ChaCha(seed=seed, rounds=self.cha_cha_generator_rounds))
        return ''.join(str(self.generator.integers(self.seed_value_lower_bound, self.seed_value_upper_bound, endpoint=True)) for _ in range(self.challenge_rounds))

    def generate_seeds(self, n: int) -> list:
        """Generate a list random seeds to distribute to new users.

        Args:
            n (int): The number of seeds to generate.

        Returns:
            list: The generated seeds.
        """
        return [secrets.SystemRandom().randrange(10 ** (self.seed_length - 1), 10 ** self.seed_length) for _ in range(n)]

    @property
    def seed_length(self) -> int:
        return self.__seed_length

    @seed_length.setter
    def seed_length(self, length: int):
        try:
            self.__seed_length = max(min(length, 18), 1)
        except TypeError:
            raise TypeError('seed length should be an integer')
        except Exception as e:
            raise e

    @property
    def challenge_rounds(self) -> int:
        return self.__challenge_rounds

    @challenge_rounds.setter
    def challenge_rounds(self, rounds: int):
        if type(rounds) is int:
            self.__challenge_rounds = max(rounds, 1)
        else:
            raise TypeError('challenge rounds should be an integer')

    @property
    def scramble_rounds(self) -> int:
        return self.__scramble_rounds

    @scramble_rounds.setter
    def scramble_rounds(self, rounds: int):
        if type(rounds) is int:
            self.__scramble_rounds = max(rounds, 0)
        else:
            raise TypeError('scramble rounds should be an integer')

    @property
    def seed_value_lower_bound(self) -> int:
        return self.__seed_value_lower_bound

    @seed_value_lower_bound.setter
    def seed_value_lower_bound(self, lower_bound: int):
        if type(lower_bound) is int:
            self.__seed_value_lower_bound = max(lower_bound, 0)
        else:
            raise TypeError('seed value lower bound should be an integer')

    @property
    def seed_value_upper_bound(self) -> int:
        return self.__seed_value_upper_bound

    @seed_value_upper_bound.setter
    def seed_value_upper_bound(self, upper_bound: int):
        if type(upper_bound) is int:
            self.__seed_value_upper_bound = max(upper_bound, 0)
        else:
            raise TypeError('seed value upper bound should be an integer')

    @property
    def cha_cha_generator_rounds(self) -> int:
        return self.__cha_cha_generator_rounds

    @cha_cha_generator_rounds.setter
    def cha_cha_generator_rounds(self, rounds: int):
        if type(rounds) is int:
            self.__cha_cha_generator_rounds = max(rounds, 1)
        else:
            raise TypeError('cha cha generator rounds should be an integer')

    @property
    def current_seed(self) -> int:
        """Return the LASTEST updated seed value stored in the syncseed generator"""
        return self.__new_seed
