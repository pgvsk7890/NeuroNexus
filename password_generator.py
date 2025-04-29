import random
import string
def generate_password(length):
    # Define character sets: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length:"))
        
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print(f"Your generated password is:{password}")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
