username = "admin"
password = "password123"


firstname = input("username: ")
user_password = input("password: ")


def login(username, password):

    if username == firstname and password == user_password:

        print(f"You've successfully logged in as {username}")

    else:

        print("Invalid credentials")


login(username, password)