import random
import string

def generate_password(length, complexity):
    # Define the possible character sets based on complexity
    char_sets = {
        1: string.ascii_lowercase,  # Lowercase letters
        2: string.ascii_lowercase + string.ascii_uppercase,  # Lowercase + Uppercase
        3: string.ascii_lowercase + string.ascii_uppercase + string.digits,  # Lowercase + Uppercase + Digits
        4: string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation  # Lowercase + Uppercase + Digits + Symbols
    }
    
    # Select the character set based on the chosen complexity
    char_set = char_sets.get(complexity, char_sets[1])
    
    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password

def password_generator():
    print("Password Generator")
    
    # Prompt user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4 characters): "))
            if length < 4:
                print("Password length must be at least 4 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Prompt user for the complexity of the password
    print("\nSelect password complexity:")
    print("1. Lowercase letters")
    print("2. Lowercase and Uppercase letters")
    print("3. Lowercase, Uppercase, and Digits")
    print("4. Lowercase, Uppercase, Digits, and Symbols")
    
    while True:
        try:
            complexity = int(input("Enter choice (1/2/3/4): "))
            if complexity not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a valid complexity option.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Generate and display the password
    password = generate_password(length, complexity)
    print(f"\nGenerated Password: {password}")

# Run the password generator
password_generator()
