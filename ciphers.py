import string
import random

class Cipher:

    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_rev = self.alphabet[::-1]

    def encrypt(self, text):
        raise NotImplementedError()

    def decrypt(self, text):
        raise NotImplementedError()

    def get_padding_chars(self, num_chars):
        padding_chars = []

        for _ in range(num_chars):
            padding_chars.append(chr(random.randrange(33,47)))

        return "".join(padding_chars)

    def char_blocks(self, encryption):
        """Output is displayed in 5 char blocks, with padding added as required.
        Sample output: The quick brown fox. = LFDKA NMYML K1KZE &XPQR
        """

        list_len = len(encryption)

        if list_len % 5 > 0:
            last_block_len = list_len % 5
            encryption += self.get_padding_chars(5 - last_block_len)

        split_encryption = [encryption[i:i+5] for i in range(0, len(encryption), 5)]

        return " ".join(split_encryption)

    @staticmethod
    def remove_char_blocks(decryption):
        decryption = ["" if not char.isalpha() else char for char in decryption]

        return "".join(decryption).replace(" ", "")

    def create_pad(self, text, keyword, encrypt=True):
        """Pad is a key that adds numbers of letters in key to correspond letter numbers of encrypted message
        to create a new encrypted message.
        """

        text = text.lower()
        keyword = keyword.lower()
        keyword = keyword[:len(text)]  # we only need the letters that correspond to the text value

        pad = []
        for i in range(len(keyword)):
            if encrypt:
                keyword_num_val = (self.alphabet.index(text[i]) + self.alphabet.index(keyword[i])) % 26
            else:
                keyword_num_val = (self.alphabet.index(text[i]) - self.alphabet.index(keyword[i])) % 26

            new_letter = self.alphabet[keyword_num_val]

            pad.append((text[i], new_letter))

        return pad

    def use_pad(self, text, keyword, encrypt=True):
        """Reads pad to encrypt or decrypt message
        """

        text = text.lower()
        pad = self.create_pad(text, keyword, encrypt=encrypt)

        encrypted_text = []

        for i in range(len(text)):
            encrypted_text.append(pad[i][1])
            i += 1

        return "".join(encrypted_text).upper()
