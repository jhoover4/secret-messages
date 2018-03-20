from ciphers import Cipher


class Affine(Cipher):

    def __init__(self, start_num, end_num, **kwargs):
        super().__init__()

        # create the affine dictionary to encode/decode message
        self.affine_dict = {}
        for i in range(26):
            affine_val = (int(start_num) * i + int(end_num)) % 26
            self.affine_dict[self.alphabet[i]] = self.alphabet[affine_val]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self, text):
        """Encryption for Affine:
        Each letter value is multiplied
        by 5 add 8, modulo 26.
        """

        text = text.lower()

        encrypted_text = [self.affine_dict[letter] for letter in text]

        return "".join(encrypted_text).upper()

    def decrypt(self, text):
        """Decryption for Affine:
        Do the reverse by subtracting 8 from value of
        letter multiplying by 21 then modulo 26.
        """

        text = text.lower()
        decrypted_text = []

        for letter in text:
            for key, val in self.affine_dict.items():
                if letter == val:
                    decrypted_text.append(key)

        return "".join(decrypted_text).upper()
