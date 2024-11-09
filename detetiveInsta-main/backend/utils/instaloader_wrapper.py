import instaloader

def create_instaloader(proxy=None):
    L = instaloader.Instaloader()
    if proxy:
        L.context.proxy = proxy
    return L
