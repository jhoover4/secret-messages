import os

from affine import Affine
from atbash import Atbash
from bifid import Bifid
from caesar import Caesar


def clear():
    """Clears screen"""

    os.system('cls' if os.name == 'nt' else 'clear')


def user_interface():
    """Command line menu providing an option to either encrypt or decrypt a value.
    Add input settings required to perform the cipher process"""

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

            if encrypt_val == 'q':
                break

            print("\nYour decrypted value is: {}\n".format(decrypt_val))

        input("Press Enter to continue...")


def run_cipher(encrypt=True):
    """Sub menu with a list of implemented ciphers"""

    clear()
    prompt = "Choose a cipher to use:\n\n"
    prompt += "1) (Af)fine\n"
    prompt += "2) (At)bash\n"
    prompt += "3) (B)ifid\n"
    prompt += "4) (C)aesar\n\n"
    prompt += "Type (q) to quit.\n"

    user_input = str(input(prompt))

    affine_input = [1, '1', 'af']
    atbash_input = [2, '2', 'at']
    bifid_input = [3, '3', 'b']
    caesar_input = [4, '4', 'c']
    valid_input = affine_input + atbash_input + bifid_input + caesar_input

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

    if user_input in affine_input:
        cipher = Affine()

    if user_input in atbash_input:
        cipher = Atbash()

    if user_input in bifid_input:
        cipher = Bifid()

    if user_input in caesar_input:
        cipher = Caesar()

    if encrypt:
        val = cipher.encrypt(text)
    else:
        val = cipher.decrypt(text)

    return cipher.char_blocks(val)


def pad_option():
    """Option for pad to add additional encryption"""

    # TODO: complete pad functionality

    prompt = "Please enter the pad number:\n\n"
    user_input = str(input(prompt))

    while user_input.lower().isalpha() is False:
        print("Value must contain letters only.\n")

        user_input = str(input(prompt))


if __name__ == "__main__":
    user_interface()
