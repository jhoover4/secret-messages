from affine_cipher import Affine
from atbash_cipher import Atbash
from bifid_cipher import Bifid


def user_interface():
    """Command line menu providing an option to either encrypt or decrypt a value.
    Add input settings required to perform the cipher process"""

    while True:
        prompt = "Choose an option:\n\n"
        prompt += "1) Encrypt\n"
        prompt += "2) Decrypt\n\n"
        prompt += "Type 'q' to quit."

        user_input = input(prompt).strip()

        if user_input.lower() == "q":
            break

        while user_input != "1" or user_input != "2":
            user_input = input(prompt).strip()

        if user_input == "1":
            run_cipher()

        if user_input == "2":
            run_cipher(encrypt=False)


def run_cipher(encrypt=True):
    """Sub menu with a list of implemented ciphers"""

    prompt = "Choose a cipher to use:\n\n"
    prompt += "1) Affine\n"
    prompt += "2) Atbash\n"
    prompt += "3) Bifid\n"

    user_input = input(prompt)
    text = input("Enter value:\n\n").replace(" ", "")

    if user_input == "1":
        return Affine.encrypt(text)

    if user_input == "2":
        return Atbash.encrypt(text)

    if user_input == "3":
        return Bifid.encrypt(text)
