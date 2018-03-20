import unittest

from affine import Affine
from atbash import Atbash
from caesar import Caesar
from keyword_cipher import Keyword
from ciphers import Cipher


class CipherTests(unittest.TestCase):
    def setUp(self):
        self.test_word = 'testy'
        self.pad_word = 'loose'

        self.cipher = Cipher()
        self.affine = Affine(5, 9)
        self.atbash = Atbash()
        self.caesar = Caesar()
        self.keyword_cipher = Keyword(self.pad_word)

    def test_char_blocks(self):
        assert self.cipher.char_blocks('testytestytest') == 'testy testy test'

    def test_use_pad(self):
        assert self.cipher.use_pad(self.test_word, self.pad_word) == 'ESGLC'

    def test_affine_encrypt(self):
        """Affine examples from http://crypto.interactive-maths.com/affine-cipher.html."""

        assert self.affine.encrypt(self.test_word) == 'ADVAZ'

    def test_affine_decrypt(self):
        """Affine examples from http://crypto.interactive-maths.com/affine-cipher.html."""

        assert self.affine.decrypt('ADVAZ') == self.test_word.upper()

    def test_atbash_encrypt(self):
        """Atbash examples from http://crypto.interactive-maths.com/atbash-cipher.html."""

        assert self.atbash.encrypt(self.test_word) == 'GVHGB'

    def test_atbash_decrypt(self):
        """Atbash examples from http://crypto.interactive-maths.com/atbash-cipher.html."""

        assert self.atbash.decrypt('GVHGB') == self.test_word.upper()

    def test_caesar_encrypt(self):
        """Caesar shifts by 3 every time.
        Caesar cipher examples from http://crypto.interactive-maths.com/caesar-cipher.html."""

        assert self.caesar.encrypt(self.test_word) == 'WHVWB'

    def test_caesar_decrypt(self):
        """Caesar shifts by 3 every time.
        Caesar cipher examples from http://crypto.interactive-maths.com/caesar-cipher.html."""

        assert self.caesar.decrypt('WHVWB') == self.test_word.upper()

    def test_keyword_encrypt(self):
        assert self.keyword_cipher.encrypt(self.test_word) == 'TARTY'

    def test_keyword_decrypt(self):
        assert self.keyword_cipher.decrypt('TARTY') == self.test_word.upper()


if __name__ == '__main__':
    unittest.main()
