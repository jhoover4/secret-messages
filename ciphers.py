import string


class Cipher:

    def __init__(self, keyword=None):
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_rev = self.alphabet[::-1]

    def encrypt(self, text):
        raise NotImplementedError()

    def decrypt(self, text):
        raise NotImplementedError()

    def char_blocks(self, encryption, padding=' '):
        """output is displayed in 5 char blocks, with padding added as required. For
            example: The quick brown fox. = LFDKA NMYML K1KZE &XPQR"""

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
                rest_of_list = (list_len - beg_count) + 1

                blocks.append(encryption[rest_of_list:])

            return padding.join(blocks)

    def remove_char_blocks(self, decryption, padding=' '):
        return decryption.replace(padding, "")
