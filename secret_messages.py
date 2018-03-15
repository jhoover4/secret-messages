import os

from affine import Affine
from atbash import Atbash
from caesar import Caesar
from keyword_cipher import Keyword


def clear():
    """Clears screen"""

    os.system('cls' if os.name == 'nt' else 'clear')


def user_interface():
    """Command line menu providing an option to either encrypt or decrypt a value.
    Add input settings required to perform the cipher process.
    """

    global encrypt_val
    while True:
        clear()

        prompt = "Welcome to the Secret Messages project for the Treehouse Techdegree!\n\n"
        prompt += "Choose an option:\n"
        prompt += "1) (E)ncrypt\n"
        prompt += "2) (D)ecrypt\n\n"
        prompt += "Type (q) to quit.\n"

        user_input = str(input(prompt)).strip()

        if user_input.lower() == "q":
            break

        encrypt_input = [1, '1', 'e']
        decrypt_input = [2, '2', 'd']
        valid_input = encrypt_input + decrypt_input

        while user_input not in valid_input:
            user_input = input(prompt).strip()

        if user_input in encrypt_input:
            encrypt_val = run_cipher()

            if encrypt_val == 'q':
                break

            print("\nYour encrypted value is: {}\n\n".format(encrypt_val))

        if user_input in decrypt_input:
            decrypt_val = run_cipher(encrypt=False)

            if decrypt_val == 'q':
                break

            print("\nYour decrypted value is: {}\n".format(decrypt_val))

        input("Press any key to continue.")


def run_cipher(encrypt=True):
    """Sub menu with a list of implemented ciphers"""

    clear()
    prompt = "Choose a cipher to use:\n\n"
    prompt += "1) (Af)fine\n"
    prompt += "2) (At)bash\n"
    prompt += "3) (C)aesar\n"
    prompt += "4) (K)eyword\n\n"
    prompt += "Type (q) to quit.\n"

    user_input = str(input(prompt))

    affine_input = [1, '1', 'af']
    atbash_input = [2, '2', 'at']
    caesar_input = [3, '4', 'c']
    keyword_cipher_input = [4, '3', 'k']
    valid_input = affine_input + atbash_input + keyword_cipher_input + caesar_input

    if user_input.lower() == "q":
        return "q"

    while user_input not in valid_input:
        user_input = str(input(prompt))

    def ask_for_value():
        return str(input("Enter value:\n").replace(" ", ""))

    text = ask_for_value()

    while text.lower().isalpha() is False:
        print("Value must contain letters only.\n")
        text = ask_for_value()

    # Affine inputs
    if user_input in affine_input:
        aff_first_number = input("Please enter a beginning number for the Affine cipher (must be odd):\n")
        aff_second_number = input("Please enter an ending number for the Affine cipher:\n")

        while aff_first_number.isnumeric() is False \
                or int(aff_first_number) % 2 == 0 \
                or aff_second_number.isnumeric() is False:
            print("Value must contain numbers. First number must be odd.\n")
            aff_first_number = input("Please enter a beginning number for the Affine Cipher (must be odd):\n")
            aff_second_number = input("Please enter an ending number for the Affine cipher:\n")

        cipher = Affine(aff_first_number, aff_second_number)

    # Atbash inputs
    if user_input in atbash_input:
        cipher = Atbash()

    # Keyword inputs
    if user_input in keyword_cipher_input:
        user_keyword = input("Please enter your keyword for the Keyword Cipher:\n")

        while text.lower().isalpha() is False:
            print("Value must contain letters only.\n")
            user_keyword = input("Please enter keyword for the Keyword Cipher:\n")

        cipher = Keyword(user_keyword)

    if user_input in caesar_input:
        cipher = Caesar()

    if encrypt:
        text = cipher.encrypt(text)
        if input("Do you want to add a secret pad? (Y/n)\n").lower() == "y":
            text = pad_option(text, cipher)

        val = cipher.char_blocks(text)
    else:
        text = cipher.remove_char_blocks(text)
        if input("Was a secret pad used? (Y/n)\n").lower() == "y":
            text = pad_option(text, cipher, encrypt=False)

        val = cipher.decrypt(text)

    return val


def pad_option(text, cipher, encrypt=True):
    """Option for pad to add additional encryption."""

    prompt = "Please enter the pad keyword, it must be at least ({}) letters:\n".format(len(text))
    user_input = str(input(prompt))

    while user_input.lower().isalpha() is False:
        print("Value must contain letters only.\n")

        user_input = str(input(prompt))

    if encrypt:
        return cipher.use_pad(text, user_input)
    else:
        return cipher.use_pad(text, user_input, encrypt=False)


if __name__ == "__main__":
    user_interface()
