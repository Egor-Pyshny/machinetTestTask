import random
import string


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            pass

    return wrapper


def generate_random_file_name():
    length = 15
    random_chars = random.choices(string.ascii_letters + string.digits, k=length)
    random_file_name = "".join(random_chars)
    return random_file_name + ".txt"
