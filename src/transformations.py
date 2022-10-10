import random


def load_random_data():  # Dummy function to load data
    return random.randint(0, 10)


def make_transformation():
    data = load_random_data()
    return data * 3


def fix_name(full_name: str) -> str:
    return " ".join(name.capitalize() for name in full_name.split())
