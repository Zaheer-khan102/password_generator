import random
import string

def generate_password():
    print("Password Generator")
    
    length = int(input("Enter the desired length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Password: ", password)
generate_password()
