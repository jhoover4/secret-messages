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

    def create_pad(self, text, keyword, encrypt = True):
        """Pad is a key that add numbers of letters in alphabet to encrypted message
        to create a new encrypted message.
        """

        text = text.lower()
        keyword = keyword.lower()
        keyword = keyword[:len(text)] # we only need the letters that correspond to the text value

        pad = {}
        for i in range(len(keyword)):
            if encrypt:
                keyword_num_val = (self.alphabet.index(text[i]) + self.alphabet.index(keyword[i])) % 26
            else:
                keyword_num_val = (self.alphabet.index(text[i]) - self.alphabet.index(keyword[i])) % 26
            new_letter = self.alphabet[keyword_num_val]

            pad[text[i]] = new_letter

        return pad

    def pad_encrypt(self, text, keyword):

        text = text.lower()
        pad = self.create_pad(text, keyword)

        if not self.pad_alphabet:
            print("Error: Pad not created. Please create a pad first.\n")
            return
        else:
            encrypted_text = [self.pad_alphabet[letter] for letter in text]



        return "".join(encrypted_text)

    def pad_decrypt(self, text, keyword):

        text = text.lower()
        pad = self.create_pad(text, keyword, encrypt=False)

        if not pad:
            print("Error: Pad not created. Please create a pad first.\n")
            return
        else:
            decrypted_text = []

            for letter in text:
                decrypted_text.append(pad[letter])

        return "".join(decrypted_text)