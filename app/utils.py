import bcrypt


def hash(password: str):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def verify_password(password: str, hashed_password: str):
    userBytes = password.encode('utf-8')
    result = bcrypt.checkpw(userBytes, hashed_password)
    return result
