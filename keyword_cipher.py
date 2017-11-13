import string

from ciphers import Cipher


class Keyword(Cipher):
    """A keyword cipher is a form of monoalphabetic substitution. A
    keyword is used as the key, and it determines the letter matchings
    of the cipher alphabet to the plain alphabet. Repeats of letters
    in the word are removed, then the cipher alphabet is generated with
    the keyword matching to A,B,C etc. until the keyword is used up,
    whereupon the rest of the ciphertext letters are used in
    alphabetical order, excluding those already used in the key.
    """

    def __init__(self):
        """Defines initial aplphabet"""
        self.alphabet = string.ascii_uppercase

    def __alphabet_generation(self, key_actual):
        """Creates a new alphabet using keyword given by user"""
        proxy1_alphabet = list(self.alphabet)

        for item in key_actual:
            if item in proxy1_alphabet:
                proxy1_alphabet.remove(item)

        proxy2_alphabet = ''.join(key_actual) + ''.join(proxy1_alphabet)

        return proxy2_alphabet

    def __key_generation(self, items):
        """Will take user defined key and remove all duplicate letters"""
        actual = []
        for item in items:
            if item not in actual:
                actual.append(item)

        return actual

    def encrypt(self):
        """This function encrypts a user input using a keyword provided by the
        user to shift the cipher, generating a new alphabet.
        """

        text = input("What would you like to encrypt?\n>> ").upper()

        key_user = list(input("Type the key you wish to use for the cipher.\n\
>> ").upper())
        key_actual = self.__key_generation(key_user)

        new_alphabet = self.__alphabet_generation(key_actual)

        Proxy_text = [(ord(x) - 65) for x in text]
        encrypted_text = ''.join([(" " if x < 0 else (new_alphabet[x]))
                                  for x in Proxy_text])

        return encrypted_text

    def decrypt(self):
        """This function decrypts a user input given the keyword used to encr\
        ypt."""

        text = input("What would you like to decrypt?\n>> ").upper()

        key_user = list(input("Type the key you wish to use for the cipher.\n\
>> ").upper())
        key_actual = self.__key_generation(key_user)

        new_alphabet = self.__alphabet_generation(key_actual)

        proxy_text = [(new_alphabet.index(x) if x in new_alphabet else " ")
                      for x in text]
        decrypted_text = ''.join([(" " if x == " " else (self.alphabet[x]))
                                  for x in proxy_text])

        return decrypted_text
