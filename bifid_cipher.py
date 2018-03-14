from cipher import Cipher


class Bifid(Cipher):

    def __init__(self, **kwargs):
        super().__init__()

        self.polybius = ['bgwkz', 'qpnds', 'ioaxe', 'fclum', 'thyvr']

        for key, value in kwargs.items():
            setattr(self, key, value)

    def find_cords(self, word):
        """Finds coordinates in polybius using inputted string"""

        cords = []

        for letter in word:
            i = 0
            for _ in range(len(self.polybius)):
                if letter in self.polybius[i]:
                    x_cord = i
                    y_cord = self.polybius[i].index(letter)

                    cord_tuple = (x_cord, y_cord)

                    cords.append(cord_tuple)

                i += 1

        return cords

    def find_string(self, cords):
        """Encryption for Bifid:
        Creates string from polybius values using cords"""

        final_str = ''

        for cord in cords:
            letter = self.polybius[cord[0]][cord[1]]
            final_str += letter

        return final_str

    def encrypt(self, text):
        """Encryption for Bifid:

        """

        self.orig_cords = self.find_cords(text)

        # coordinates are added together as strings to make a new number
        x_cords = [x for (x, y) in self.orig_cords]
        y_cords = [y for (x, y) in self.orig_cords]
        adj_cords = x_cords + y_cords
        adj_cords_end = len(adj_cords) + 1

        encrypt_cords = zip(adj_cords[0:adj_cords_end:2], adj_cords[1:adj_cords_end:2])

        encrypted_val = self.find_string(encrypt_cords)

        return encrypted_val

    def decrypt(self, text):
        """Decryption for Bifid:

        """

        # TODO: Complete Bifid decryption

        decypted_val = ''

        return decypted_val


if __name__ == "__main__":
    # for debugging purposes

    test = Bifid()
    b = test.encrypt('verylongword')
