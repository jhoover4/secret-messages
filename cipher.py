import string

#### INSTRUCTIONS ####

# provide a command line menu providing an
# option to either encrypt or decrypt a value and
# then a sub menu with a list of implemented ciphers

# write a seperate class, which inherits from cipher,
# and implements encrypt and decrypt functionality for reach
# of your chosen ciphers

# prompt the user for input to enc or dec and , if aplicable
# any add input settings required to perform the cipher
# process

# remember to include docstrings

# make sure to follow PEP 8


class Cipher:

    def __init__(self, keyword=None):
        # added by Jordan
        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_rev = self.alphabet[::-1]

    def encrypt(self, text):
        raise NotImplementedError()

    def decrypt(self, text):
        raise NotImplementedError()

    def char_blocks(self, encryption, padding=' '):
        """output is displayed in 5 char blocks, with padding added as required. For
            example: The quick brown fox. = LFDKA NMYML K1KZE &XPQR"""

        blocks = []
        beg_count = 0
        end_count = 5
        list_len = len(encryption) + 1

        while end_count < list_len:
            blocks.append(encryption[beg_count:end_count])

            end_count += 5
            beg_count += 5
        if end_count != list_len:
            rest_of_list = list_len - beg_count

            blocks.append(encryption[rest_of_list:])

        return padding.join(blocks)
