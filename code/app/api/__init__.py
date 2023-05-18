import random, string


def create_short_url(prefix):
    """
    Just a simple short url generator.

    :return: random short url
    """
    return "http://" + prefix + '/' + ''.join(random.choice(string.ascii_lowercase) for i in range(5))
