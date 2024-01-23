import random
import string

def generate_password(words, length=12, include_special_chars=False):
    """
    Generate a random password by combining user-provided words with random characters.

    Parameters:
    - words: List of words provided by the user.
    - length: Desired length of the password (default is 12).
    - include_special_chars: Boolean flag indicating whether to include special characters.

    Returns:
    A randomly generated password.
    """
    # Combine user-provided words with random characters
    word_part = ''.join(words)
    remaining_length = length - len(word_part)

    # Define character sets (letters and digits by default)
    character_set = string.ascii_letters + string.digits

    # Include special characters if specified by the user
    if include_special_chars:
        character_set += string.punctuation

    # Generate random characters for the remaining length
    random_part = ''.join(random.choices(character_set, k=remaining_length))

    # Shuffle the combined parts to enhance randomness
    password = ''.join(random.sample(word_part + random_part, len(word_part + random_part)))

    return password

def main():
    # Welcome message
    print("Welcome to the Random Password Generator")

    # Get user input for words to include in the password
    words = input("Enter some words to include in the password (separated by spaces): ").split()
    if not words:
        print("Please enter at least one word.")
        return

    # Get user input for the desired password length
    password_length = int(input("Enter the desired password length: "))
    if password_length < len(words):
        print("Password length should be equal to or greater than the total length of input words.")
        return

    # Ask the user if special characters should be included in the password
    include_special_chars = input("Include special characters in the password? (y/n): ").lower() == 'y'

    # Generate and display the password
    generated_password = generate_password(words, password_length, include_special_chars)
    print("\nGenerated Password:", generated_password)

if __name__ == "__main__":
    main()
