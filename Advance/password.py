import secrets, string

def generate_password(length=8, use_punctuation=True):
    if length <= 0:
        raise ValueError("length must be > 0")
    a = string.ascii_letters + string.digits + (string.punctuation if use_punctuation else "")
    return ''.join(secrets.choice(a) for _ in range(length))


if __name__ == '__main__':
    print("Password:", generate_password(8))