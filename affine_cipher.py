import string

from ciphers import Cipher


class Affine(Cipher):
    """The affine cipher is a type of monoalphabetic substitution
    cipher, wherein each letter in an alphabet is mapped to its numeric
    equivalent, encrypted using a simple mathematical function, and
    converted back to a letter. Each letter is enciphered with the
    function (ax + b) mod 26, where b is the magnitude of the shift.
    """

    def __init__(self):
        """Defines initial aplphabet."""
        self.alphabet = string.ascii_uppercase
        self.mod26 = {letter: number for letter,
                      number in zip([item for item in self.alphabet],
                                    [num for num in range(0, 26)])}
        self.mod26_inverse = {number: letter for number,
                              letter in zip([num for num in range(0, 26)],
                                            [item for item in self.alphabet])}

    def encrypt(self):
        """encryption function E(x)= (ax+b)mod26"""
        text = input("What would you like to encrypt?\n>> ").upper()
        proxy_text = [letter for letter in text.replace(" ", "")]
        encrypted_text = [str(self.mod26[letter]) for letter in proxy_text]

        return ' '.join(encrypted_text)

    def decrypt(self):
        """decryption function D(x) = a^(-1)(x-b)mod26"""
        text = input("What would you like to decrypt?\nBe sure to separate nu\
mbers with a space!\n>> ").upper()
        proxy_text = [int(item) for item in text.split(' ')]
        decrypted_text = [self.mod26_inverse[number] for number in proxy_text]

        return ''.join(decrypted_text)
