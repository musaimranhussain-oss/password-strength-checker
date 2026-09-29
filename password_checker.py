COMMON_PASSWORDS = [
    "password",
    "password123",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "letmein",
    "welcome",
    "admin",
    "admin123",
    "football",
    "football123",
    "iloveyou",
    "monkey",
    "abc123"
]


def check_length(password):
    """Return True if password is at least 8 characters long."""
    return len(password) >= 8


def check_uppercase(password):
    """Return True if password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)


def check_lowercase(password):
    """Return True if password contains at least one lowercase letter."""
    return any(char.islower() for char in password)


def check_number(password):
    """Return True if password contains at least one digit."""
    return any(char.isdigit() for char in password)


def check_special_character(password):
    """Return True if password contains at least one special character."""
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>/?"
    return any(char in special_characters for char in password)


def check_common_password(password):
    """Return True if password is NOT in the list of common passwords."""
    return password.lower() not in COMMON_PASSWORDS


def check_password(password):
    """Run all checks on a password and return its score, rating and checks."""

    if password is None:
        raise ValueError("Password cannot be None.")

    checks = {
        "At least 8 characters": check_length(password),
        "Contains uppercase letter": check_uppercase(password),
        "Contains lowercase letter": check_lowercase(password),
        "Contains a number": check_number(password),
        "Contains special character": check_special_character(password),
        "Not a common password": check_common_password(password)
    }

    score = sum(checks.values())

    # Rating boundaries: 0-2 = Weak, 3-4 = Medium, 5-6 = Strong.
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return score, rating, checks


def main():
    """Ask the user for a password and display its strength."""

    password = input("Enter a password to check: ")

    if not password:
        print("Password cannot be empty.")
        return

    score, rating, checks = check_password(password)

    print("\nPassword Strength:", rating)
    print("Score:", score, "/ 6")

    print("\nChecks:")
    for check, passed in checks.items():
        symbol = "✓" if passed else "✗"
        print(symbol, check)


if __name__ == "__main__":
    main()
