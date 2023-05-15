import random, string


def create_short_url():
    """
    Just a simple sort url generator.

    :return: random url
    """
    return "http://localhost:8000/" + ''.join(random.choice(string.ascii_lowercase) for i in range(5))
