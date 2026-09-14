def check_length(password) : 
  return len(password) >= 8 
  
def check_uppercase(password) :
  return any(char.isupper() for char in password)
print(check_uppercase("password"))
print(check_uppercase("Password"))
