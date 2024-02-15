import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    byte_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_password, salt)
    return hashed_password
