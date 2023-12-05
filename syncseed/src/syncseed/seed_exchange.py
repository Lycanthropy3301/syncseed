import secrets
import syncseed

class SyncseedExchangeAlgorithm():

    __gen = syncseed.SyncseedGenerator()

    def __init__(self):
        self.seed_length = 18
        self.transform_rounds = 0

    def parity_transformation(self, seed_1: int, seed_2: int, nonce_1: int = 0, nonce_2: int = 0) -> tuple[int, int]:
        """Perform a parity transformation on the input seeds and nonces.

        Args:
            seed_1 (int): The first user's seed.
            seed_2 (int): The second user's seed.
            nonce_1 (int): The first user's nonce. This defaults to 0, which has no effect on the transformation.
            nonce_2 (int): The first user's nonce. This defaults to 0, which has no effect on the transformation.

        Returns:
            int, int: The transformations to be sent to users.
        """

        self._SyncseedExchangeAlgorithm__validate_transformation(seed_1, seed_2)

        hidden_seed = secrets.SystemRandom().randrange(10 ** (self.seed_length - 1), 10 ** self.seed_length)

        transformation_1 = seed_1 ^ hidden_seed ^ nonce_1
        transformation_2 = seed_2 ^ hidden_seed ^ nonce_2

        del hidden_seed

        return transformation_1, transformation_2


    def extract_parity(self, seed: int, transformation: int, nonce: int = 0, mutate: bool = False) -> int:
        """Extract the original seed from a parity transformation

        Args:
            seed (int): The user's seed.
            nonce (int): The user's nonce. This defaults to 0, which has no effect on the extraction.
            mutate (bool): Whether or not to mutate the seed after extraction. Set to False by default.

        Returns:
            int: The extracted seed.
        """

        self._SyncseedExchangeAlgorithm__validate_extraction(seed, transformation)

        extracted_seed = seed ^ nonce ^ transformation

        self.__gen.get_expected_seed_value(extracted_seed)

        for _ in range(self.transform_rounds):
            extracted_seed = self.__gen.update_seed()

        if mutate:
            return self.__gen.mutate_seed(extracted_seed)
        else:
            return extracted_seed

    def exchange_transformation(self, seed_1: int, seed_2: int, nonce_1: int = 0, nonce_2: int = 0) -> tuple[int, int]:
        """Perform an exchange transformation on the input seeds and nonces.

        Args:
            seed_1 (int): The first user's seed.
            seed_2 (int): The second user's seed.
            nonce_1 (int): The first user's nonce. This defaults to 0, which has no effect on the transformation.
            nonce_2 (int): The first user's nonce. This defaults to 0, which has no effect on the transformation.

        Returns:
            int: The transformations to be sent to users.
        """

        self._SyncseedExchangeAlgorithm__validate_transformation(seed_1, seed_2)

        transformation_1 = seed_1 ^ seed_2 ^ nonce_1
        transformation_2 = seed_1 ^ seed_2 ^ nonce_2

        return transformation_1, transformation_2

    def extract_exchange(self, seed: int, transformation: int, nonce: int = 0) -> int:
        """Extract the original seed from a exchange transformation

        Args:
            seed (int): The user's seed.
            nonce (int): The user's nonce. This defaults to 0, which has no effect on the extraction.

        Returns:
            int: The extracted seed.
        """

        self._SyncseedExchangeAlgorithm__validate_extraction(seed, transformation)

        extracted_seed = seed ^ transformation ^ nonce

        return extracted_seed

    def selection_transformation(self, seed_1: int, seed_2: int, nonce_1: int = 0, nonce_2: int = 0) -> tuple[int, int]:
        """Perform a tree transformation on the input seeds and nonces.

        Args:
            seed_1 (int): The first user's seed.
            seed_2 (int): The second user's seed.
            nonce_1 (int): The first user's nonce. This defaults to 0, which has no effect on the transformation.
            nonce_2 (int): The first user's nonce. This defaults to 0, which has no effect on the transformation.

        Returns:
            int: The transformations to be sent to users.
        """

        self._SyncseedExchangeAlgorithm__validate_transformation(seed_1, seed_2)

        chosen_seed = secrets.SystemRandom().choice([seed_1, seed_2])

        self.__gen.get_expected_seed_value(seed_1)
        updated_seed_1 = self.__gen.update_seed()
        self.__gen.get_expected_seed_value(seed_2)
        updated_seed_2 = self.__gen.update_seed()

        transformation_1 = nonce_1 ^ chosen_seed ^ updated_seed_1
        transformation_2 = nonce_2 ^ chosen_seed ^ updated_seed_2

        return int(transformation_1), int(transformation_2)

    def extract_selection(self, seed: int, transformation: int, nonce: int = 0) -> int:
        """Extract the original seed from a tree transformation

        Args:
            seed (int): The user's seed.
            nonce (int): The user's nonce. This defaults to 0, which has no effect on the extraction.

        Returns:
            int: The extracted seed.
        """

        self._SyncseedExchangeAlgorithm__validate_extraction(seed, transformation)

        self.__gen.get_expected_seed_value(seed)

        extracted_seed = transformation ^ nonce ^ self.__gen.update_seed()

        return extracted_seed


    def __validate_transformation(self, seed_1, seed_2):

        if not(type(seed_1) is int) or not(type(seed_2) is int):
            raise TypeError("Both seeds must be integers!")

        if len(str(seed_1)) != self.seed_length or len(str(seed_2)) != self.seed_length:
            raise ValueError("Seeds are not of the correct length!")

    def __validate_extraction(self, seed, transformation):
        if not(type(seed) is int) or not(type(transformation) is int):
            raise TypeError("Both seed and transformation must be integers!")

    @property
    def seed_length(self) -> int:
        return self.__seed_length

    @seed_length.setter
    def seed_length(self, length: int):
        try:
            self.__seed_length = max(min(length, 18), 1)
            self.__gen.seed_length = max(min(length, 18), 1)
        except TypeError:
            raise TypeError('seed length should be an integer')
        except Exception as e:
            raise e

    @property
    def transform_rounds(self) -> int:
        return self.__transform_rounds

    @transform_rounds.setter
    def transform_rounds(self, rounds: int):
        try:
            self.__transform_rounds = max(rounds, 0)
        except TypeError:
            raise TypeError('seed length should be an integer')
        except Exception as e:
            raise e
