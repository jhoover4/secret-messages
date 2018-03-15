from ciphers import Cipher


class Affine(Cipher):

    def __init__(self, start_num, end_num, **kwargs):
        super().__init__()

        def affine(start_num, end_num):

            affine_dict = {}

            for i in range(26):
                affine_val = (start_num * i + end_num) % 26

                affine_dict[self.alphabet(i)] = self.alphabet[affine_val]

            return affine_dict

        self.affine_alphabet = affine(start_num, end_num)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self, text):
        """Encryption for Affine:
        Each letter value is multiplied
        by 5 and then add 8 then mod 26 as if the value is greater than 26 we
        loop around
        """

        text = text.lower()

        encrypted_text = [self.affine_alphabet[letter] for letter in text]

        return "".join(encrypted_text).upper()

    def decrypt(self, text):
        """Decryption for Affine:
        Do the reverse by subtracting 8 from value of
        letter multiplying by 21 then mod 26 to loop around
        """

        text = text.lower()

        decrypted_text = []

        for letter in text:
            for key, val in self.affine_alphabet.items():
                if letter == val:
                    decrypted_text.append(key)

        return "".join(decrypted_text).upper()


if __name__ == "__main__":
    # for debugging purposes

    test = Affine(5, 8)
    test.encrypt('word')
    test.decrypt('oapx')
