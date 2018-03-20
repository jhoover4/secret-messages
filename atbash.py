from ciphers import Cipher


class Atbash(Cipher):

    def __init__(self, **kwargs):
        super().__init__()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self, text):
        """Encryption for Atbash:
        Maps letter in alphabet to its reverse
        """

        text = text.lower()

        alpha_pos = [self.alphabet.index(letter) for letter in text]
        encrypted_val = "".join([self.alphabet_rev[int(pos)] for pos in alpha_pos])

        return encrypted_val.upper()

    def decrypt(self, text):
        """Decryption for Atbash:
        To return your original input, reference the input_val attribute
        """

        text = text.lower()

        alpha_pos = [self.alphabet_rev.index(letter) for letter in text]
        decrypted_val = "".join([self.alphabet[int(pos)] for pos in alpha_pos])

        return decrypted_val.upper()


if __name__ == "__main__":
    pass
