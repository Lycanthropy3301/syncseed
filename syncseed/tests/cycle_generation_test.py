import syncseed.syncseed as syncseed
import time
import threading

def monitor_iterations():
    while not stop_event.is_set():
        time.sleep(5)
        print(f'Current number of iterations: {len(replicate_set)}')


if __name__ == "__main__":

    generator = syncseed.SyncseedGenerator()

    # Modify these as you please
    generator.seed_length = 18
    generator.challenge_rounds = 100
    generator.scramble_rounds = 0
    generator.seed_value_lower_bound = 100_000_000_000
    generator.seed_value_upper_bound = 999_999_999_999
    generator.cha_cha_generator_rounds = 20

    replicate_set = set()
    stop_event = threading.Event()

    monitor_thread = threading.Thread(target=monitor_iterations)
    monitor_thread.start()

    try:
        while True:
            seed = generator.update_seed()
            if seed in replicate_set:
                break
            else:
                replicate_set.add(seed)

    except KeyboardInterrupt:
        stop_event.set()
        monitor_thread.join()

    print(f'Cycle forms after {len(replicate_set)} iterations!')
