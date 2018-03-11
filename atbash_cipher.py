import string


from cipher import Cipher

class Atbash(Cipher):

    def __init__(self, input_val, **kwargs):
        self.input_val = input_val

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self, text):
        """maps letter in alphabet to its reverse"""

        alpha_pos = [self.alphabet.index(letter) for letter in text]
        encrypted_val = "".join([self.alphabet_rev[int(pos)] for pos in alpha_pos])

        return encrypted_val

    def decrypt(self, text):
        """returns a decrypted value.
        To return your original input, reference the input_val attribute"""

        alpha_pos = [self.alphabet_rev.index(letter) for letter in text]
        decypted_val = "".join([self.alphabet[int(pos)] for pos in alpha_pos])

        return decypted_val

if __name__ == "__main__":
    # for testing purposes