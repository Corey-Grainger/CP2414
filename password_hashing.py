import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    byte_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_password, salt)
    return hashed_password, salt


def cross_reference_hashed_password(password, hashed_password):
    byte_password = password.encode('utf-8')
    return bcrypt.checkpw(byte_password, bytes(hashed_password, 'utf-8'))

