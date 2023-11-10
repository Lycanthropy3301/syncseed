import random
import socket

with open("Users.txt", 'r') as user_file:
    users = user_file.read().split('\n')

with open("Seeds.txt", 'r') as seed_file:
    seeds = seed_file.read().split('\n')
    seeds.pop(-1)

user_password = {user.split(' ')[0]: user.split(' ')[1] for user in users}
seed_users = {seed.split(' ')[0]: (int(seed.split(' ')[1]), int(seed.split(' ')[2])) for seed in seeds}

def authenticated(user, password, seed_value):
    if password != user_password[user]:
        return False

    seed, seed_increment = seed_users[user]

    try:
        seed_value = int(seed_value)
    except Exception:
        return False

    random.seed(seed)

    for i in range(seed_increment):
        random.randint(100000000000, 999999999999)

    if seed_value == random.randint(100000000000, 999999999999):
        return True

    return False

listener = socket.socket()
listener.bind(('', 450))
listener.listen(128)

while True:
    client, address = listener.accept()
    message = client.recv(128).decode()

    if len(message.split('/')) != 3:
        client.send('Failed!'.encode())
        client.close()
        continue

    username, password, seed_value = message.split('/')

    if username not in user_password:
        client.send('Failed!'.encode())
        client.close()
        continue

    if authenticated(username, password, seed_value):
        client.send('Success!'.encode())
        seed_users[username] = (seed_users[username][0], seed_users[username][1]+1)
        with open("Seeds.txt", 'w') as seed_file:
            seed_file.write('')
        for key, value in seed_users.items():
            with open("Seeds.txt", 'a') as seed_file:
                seed_file.write(f'{key} {value[0]} {value[1]}\n')

        print(f'{username} has authenticated!')

        client.close()
    else:
        client.send('Failed!'.encode())
        client.close()
