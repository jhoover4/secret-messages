import os
import string

from affine_cipher import Affine
from atbash_cipher import Atbash
from bifid_cipher import Bifid


def clear():
    """Clears screen"""

    os.system('cls' if os.name == 'nt' else 'clear')


def user_interface():
    """Command line menu providing an option to either encrypt or decrypt a value.
    Add input settings required to perform the cipher process"""

    while True:
        clear()

        prompt = "Choose an option:\n\n"
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

            print("\nYour encrypted value is: {}\n\n".format(encrypt_val))

        if user_input in decrypt_input:
            decrypt_val = run_cipher(encrypt=False)

            print("\nYour decrypted value is: {}\n".format(decrypt_val))

        input("Press Enter to continue...")

def run_cipher(encrypt=True):
    """Sub menu with a list of implemented ciphers"""

    clear()
    prompt = "Choose a cipher to use:\n\n"
    prompt += "1) (Af)fine\n"
    prompt += "2) (At)bash\n"
    prompt += "3) (B)ifid\n"

    user_input = str(input(prompt))

    affine_input = [1, '1', 'af']
    atbash_input = [2, '2', 'at']
    bifid_input = [3, '3', 'b']
    valid_input = affine_input + atbash_input + bifid_input

    while user_input not in valid_input:
        user_input = str(input(prompt))

    def ask_for_value():
        return str(input("Enter value:\n").replace(" ", ""))

    text = ask_for_value()

    while text.lower().isalpha() is False:
        print("Value must contain letters only.\n")
        text = ask_for_value()

    if user_input in affine_input:
        cipher = Affine(text)

    if user_input in atbash_input:
        cipher = Atbash(text)

    if user_input in bifid_input:
        cipher = Bifid(text)

    return cipher.encrypt(text)

if __name__ == "__main__":
    user_interface()