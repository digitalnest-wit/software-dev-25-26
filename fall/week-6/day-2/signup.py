def validate_username(username: str):
    if len(username) < 5:
        raise ValueError("Invalid username. Must be at least 5 characters long!")

    if username[0].isdigit():
        raise ValueError("Invalid username. Cannot begin with a number!")

def validate_password(password: str):
    if len(password) < 8:
        raise ValueError("Invalid password. Must be at least 5 characters long!")

    if password == username:
        raise ValueError("Invalid password. Password must be different than username!")

while True:
    try:
        username = validate_username(input("Enter a username: "))
        password = validate_password(input("Enter a password: "))
        break
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        break
