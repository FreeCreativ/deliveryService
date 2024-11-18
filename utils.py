import random
import string


def generate_id():
    """Generate a random alphanumeric string of length 8 for the customerId"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
