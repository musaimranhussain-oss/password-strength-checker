def check_length(password) : 
  return len(password) >= 8 
  
def check_uppercase(password) :
  return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)
  
def check_number(password):
    return any(char.isdigit() for char in password)

print(check_number("Password"))
print(check_number("Password123"))
