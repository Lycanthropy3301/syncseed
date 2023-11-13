import os
import secrets

OPTIONS = '''
[1] Modify/Display config file
[2] Set up seeds and incrments
[3] Exit
'''

def get_numeric_input():
    while True:
        option = input('Enter an option choice: ')
        if option.isnumeric():
            break
        else:
            print('Invalid input!')

    return option

with open('options.cfg') as config_file:
    config_dict = {key[0].strip(): value.strip() for line in config_file if (key := line.split('=', 1)) for value in key}

with open('options.cfg') as config_file:
    config_options = {key[0].strip(): value.strip() for line in config_file if (key := line.split('=', 1)) and '[' not in key[0] and key[0].strip() for value in key}

print(OPTIONS)
option = int(get_numeric_input())

if option == 1:
    print('\nSelect all options you want to configure, seperated by spaces (just press enter if you have no changes): \n')
    for increment, key_value_pair in enumerate(config_options.items(), start=1):
        print(f'[{increment}] {key_value_pair[0]} = {key_value_pair[1]}')

    print('')

    selected_options = input('Selected options: ').split(' ')

    for char in selected_options:
        option_index = int(char) - 1
        if 0 <= option_index < len(config_options):
            selected_key = list(config_options.keys())[option_index]
            new_value = input(f'Enter a new value for {selected_key}: ')
            config_dict[selected_key] = new_value

    with open('options.cfg', 'w') as config_file:
        for key, value in config_dict.items():
            if key != value:
                config_file.write(f'{key} = {value}\n')
            else:
                config_file.write(f'{key}\n')

    print('Changes succesful, exiting program.')

elif option == 2:
    print('\nCurrent Seed Information: ')
    print(f"SEED_VALUE_LOWER_BOUND = {config_options['SEED_VALUE_LOWER_BOUND']}")
    print(f"SEED_VALUE_UPPER_BOUND = {config_options['SEED_VALUE_UPPER_BOUND']}")
    print(f"SEED_LENGTH = {config_options['SEED_LENGTH']}\n")

    option = input('Configure with these settings? [y/n] ')[0].lower()

    if option == 'y':
        SERVER_SEED_PATH = '..\\Source\\Seeds.txt'
        USER1_SEED_PATH = '..\\User1_Dir\\seed-increment.txt'
        USER2_SEED_PATH = '..\\User2_Dir\\seed-increment.txt'

        with open(SERVER_SEED_PATH) as server_seed_file:
            server_seeds = {line.split(' ')[0]: line.split(' ')[1] for line in server_seed_file}

        generator = secrets.SystemRandom()

        for key in server_seeds.keys():
            server_seeds[key] = generator.randrange(10**(int(config_options['SEED_LENGTH'])-1), (10**(int(config_options['SEED_LENGTH'])))-1)

        with open(SERVER_SEED_PATH, 'w') as server_seed_file:
            for key, value in server_seeds.items():
                server_seed_file.write(f'{key} {value} 0\n')

        with open(USER1_SEED_PATH, 'w') as user_file:
            user_file.write(f"{server_seeds['User1']} 0")

        with open(USER2_SEED_PATH, 'w') as user_file:
            user_file.write(f"{server_seeds['User2']} 0")

        print('Changes succesful, exiting program.')

    else:
        print('Exiting program.')

elif option == 3:
    print('Exiting program.')

else:
    print('Invalid option!')
