import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        character_pool += string.digits         # 0-9
    if use_symbols:
        character_pool += string.punctuation    # Special characters

    if not character_pool:
        print("Error: No character types selected.")
        return ""

    # Generate password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get password length from user
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length must be a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Ask which characters to include
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    
    if password:
        print(f"\nYour generated password: {password}")

if __name__ == "__main__":
    main()
