from argon2 import PasswordHasher


hasher = PasswordHasher()

def hash(password: str) -> str:
    """
    Returns the cipher of `plain`,
    and empty string if hashing failed
    """

    try:
        return hasher.hash(password)
    except:
        return ''


def verify(cipher: str, password: str) -> bool:
    """
    Returns `True` if the hash of `plain` is `cipher`
    Returns `False` if `plain` and `cipher` don't match, or exception was raised
    """
    try:
        return bool(hasher.verify(cipher, password))
    except:
        return False