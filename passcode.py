import random
import string


class User:
    """
    Create User class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):