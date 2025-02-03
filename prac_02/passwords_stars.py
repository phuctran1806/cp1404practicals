MINIMUM_PASSWORD_LENGTH = 10

def main():
    """Get and print the password"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print the password"""
    print("*" * len(password))


def get_password():
    """Get the valid password"""
    password = input("Enter your password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Your password is too short")
        password = input("Enter your password: ")
    return password

main()
