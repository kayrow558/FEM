import os
import random

def load_proxies(file_path='proxies.txt'):
    proxies = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]
    return proxies


def get_random_proxy(proxies):
    if proxies:
        return random.choice(proxies)
    return None
