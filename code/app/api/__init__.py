import random, string


def create_short_url(prefix):
    """
    Just a simple sort url generator.

    :return: random url
    """
    return prefix + '/' + ''.join(random.choice(string.ascii_lowercase) for i in range(5))
