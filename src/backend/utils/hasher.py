from argon2 import PasswordHasher

hasher = PasswordHasher()

def hash(plain: str) -> str:
    """
    Returns the hash of `plain`,
    and empty string if hashing failed
    """

    try:
        return hasher.hash(plain)
    except:
        return ''

def verify(cipher: str, plain: str) -> bool:
    """
    Returns `True` if the hash of `plain` is `cipher`
    Returns `False` if `plain` and `cipher` don't match, or exception was raised
    """
    try:
        return bool(hasher.verify(cipher, plain))
    except:
        return False