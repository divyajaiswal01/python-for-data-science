#Student Login System

# The program should:
# Ask for a username.
# Ask for a password.
# Username should ignore leading/trailing spaces.
# Username should be converted to lowercase.
# Password must:
# Have at least 8 characters.
# Contain one uppercase letter.
# Contain one lowercase letter.
# Contain one digit.
# If both are valid, print:

username = input("Enter the username : ")
username = username.strip().lower()
password = input("Enter the password : ")
has_uppercase = False
has_lowercase = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_uppercase = True
    elif ch.islower():
        has_lowercase = True
    elif ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_uppercase and has_lowercase and has_digit:
    print("Login successful")
    print(f"username : {username}")
else:
    print("Invalid username or password")