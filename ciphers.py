import string


class Cipher:

    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_rev = self.alphabet[::-1]

    def encrypt(self, text):
        raise NotImplementedError()

    def decrypt(self, text):
        raise NotImplementedError()

    def char_blocks(self, encryption, padding=' '):
        """Output is displayed in 5 char blocks, with padding added as required.
        Sample output: The quick brown fox. = LFDKA NMYML K1KZE &XPQR
        """

        if len(encryption) < 5:
            return encryption

        else:
            blocks = []
            beg_count = 0
            end_count = 5
            list_len = len(encryption) + 1

            while end_count < list_len:
                blocks.append(encryption[beg_count:end_count])

                end_count += 5
                beg_count += 5
            if end_count != list_len:
                blocks.append(encryption[beg_count:])

            return padding.join(blocks)

    def remove_char_blocks(self, decryption, padding=' '):
        return decryption.replace(padding, "")

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

        return "".join(encrypted_text)
