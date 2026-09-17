def check_length(password) : 
  return len(password) >= 8 
  
def check_uppercase(password) :
  return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)
  
def check_number(password):
    return any(char.isdigit() for char in password)
  
def check_special_character(password):
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>/?"
    return any(char in special_characters for char in password) 

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

def check_common_password(password):
    return password.lower() not in COMMON_PASSWORDS

def check_password(password):
    checks = {
        "At least 8 characters": check_length(password),
        "Contains uppercase letter": check_uppercase(password),
        "Contains lowercase letter": check_lowercase(password),
        "Contains a number": check_number(password),
        "Contains special character": check_special_character(password),
        "Not a common password": check_common_password(password)
    }

    score = sum(checks.values())

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return score, rating, checks

password = input("Enter a password to check: ")

score, rating, checks = check_password(password)

print("\nPassword Strength:", rating)
print("Score:", score, "/ 6")

print("\nChecks:")

for check, passed in checks.items():
    if passed:
        print("✓", check)
    else:
        print("✗", check)
