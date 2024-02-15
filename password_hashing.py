import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    byte_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_password, salt).decode('utf-8')
    return hashed_password, salt


def cross_reference_hashed_password(password, hashed_password):
    byte_password = password.encode('utf-8')
    return bcrypt.checkpw(byte_password, bytes(hashed_password, 'utf-8'))


def test_bcrypt():
    salt = bcrypt.gensalt()
    test_password = 'testpassword123@'
    byte_password = test_password.encode('utf-8')
    test_hashed_password = bcrypt.hashpw(byte_password, salt)
    print(bcrypt.checkpw(bytes(test_password, 'utf-8'), test_hashed_password), test_hashed_password, salt)

if __name__ == '__main__':
    test_bcrypt()
