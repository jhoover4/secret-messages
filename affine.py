from ciphers import Cipher


class Affine(Cipher):

    def __init__(self, **kwargs):
        super().__init__()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self, text):
        """Encryption for Affine:
        Each letter value is multiplied
        by 5 and then add 8 then mod 26 as if the value is greater than 26 we
        loop around
        """

        text = text.lower()

        pos = [(self.alphabet.index(letter) * 5) + 8 for letter in text]
        new_pos = []

        for num in pos:
            while num > 25:
                num -= 25
            new_pos.append(num)

        encrypted_val = "".join([self.alphabet[pos] for pos in new_pos])

        return encrypted_val.upper()

    def decrypt(self, text):
        """Decryption for Affine:
        Do the reverse by substracting 8 from value of
        letter multiplying by 21 then mod 26 to loop around
        """

        text = text.lower()

        pos = [(self.alphabet.index(letter) / 5) - 8 for letter in text]
        new_pos = []

        for num in pos:
            while num > 25:
                num -= 25
            new_pos.append(num)

        # TODO: finish affine decryption
        decypted_val = ''

        return decypted_val.upper()


if __name__ == "__main__":
    # for debugging purposes

    test = Affine()
    test.encrypt('word')
