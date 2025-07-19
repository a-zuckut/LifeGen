import random

def gen_life():
    """
    Generates a new life form.
    """
    # To start, first return simple 10-character string.
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
