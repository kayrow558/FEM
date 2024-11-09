import os

def load_accounts():
    accounts = []
    i = 1
    while os.getenv(f"INSTAGRAM_USER_{i}") and os.getenv(f"INSTAGRAM_PASS_{i}"):
        accounts.append({
            'username': os.getenv(f"INSTAGRAM_USER_{i}"),
            'password': os.getenv(f"INSTAGRAM_PASS_{i}")
        })
        i += 1

    if os.path.exists('accounts.txt'):
        with open('accounts.txt', 'r') as file:
            for line in file:
                user, pwd = line.strip().split(':')
                accounts.append({'username': user, 'password': pwd})
    return accounts
