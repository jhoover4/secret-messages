import string


from cipher import Cipher

class Affine(Cipher):

    def __init__(self, input_val, **kwargs):
        self.input_val = input_val

        for key, value in kwargs.items():
            setattr(self, key, value)

    def encrypt(self):
        """Uses an equation where each letter value is multiplied
        by 5 and then add 8 then mod 26 as if the value is greater than 26 we
        loop around"""

        pos = [(self.alphabet.index(letter) * 5) + 8 for letter in self.input_val]
        new_pos = []

        for num in pos:
            while num > 25:
                num -= 25
            new_pos.append(num)

        encrypted_val = "".join([self.alphabet[pos] for pos in new_pos])

        return encrypted_val

    def decrypt(self):
        """decryption for affine -  do the reverse by substracting 8 from value of
        letter multiplying by 21 then mod 26 to loop around"""

        pos = [(self.alphabet.index(letter)/ 5) - 8 for letter in self.input_val]
        new_pos = []

        for num in pos:
            while num > 25:
                num -= 25
            new_pos.append(num)

        return decypted_val

if __name__ == "__main__":
    # for debugging purposes

    test = Affine('word')
    test.encrypt()
