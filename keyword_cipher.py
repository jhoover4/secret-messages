from ciphers import Cipher


class Keyword(Cipher):

    def __init__(self, keyword, **kwargs):
        super().__init__()

        self.keyword = keyword

        alphabet_and_key = list(self.keyword) + self.alphabet[:]

        self.keyword_alphabet = []

        for letter in alphabet_and_key:
            if letter not in self.keyword_alphabet:
                self.keyword_alphabet.append(letter)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self, text):
        """Encryption for Keyword:
        Determines the letter matchings of the keyword alphabet to the plain alphabet
        """

        text = text.lower()

        text_pos = [self.alphabet.index(letter) for letter in text]

        encrypted_letters = [self.keyword_alphabet[num] for num in text_pos]

        return ''.join(encrypted_letters).upper()


    def decrypt(self, text):
        """Decryption for Keyword:
        Determines the letter matchings of the keyword alphabet to the plain alphabet
        """

        text = text.lower()

        text_pos = [self.keyword_alphabet.index(letter) for letter in text]

        decrypted_letters = [self.alphabet[num] for num in text_pos]

        return ''.join(decrypted_letters).upper()



if __name__ == "__main__":
    # for debugging purposes

    test = Keyword('crazy')
    test.encrypt('word')
    test.decrypt('word')