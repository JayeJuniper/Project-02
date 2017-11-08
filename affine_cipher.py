import string

from ciphers import Cipher


class Affine(Cipher):
    """The affine cipher is a type of monoalphabetic substitution 
    cipher, wherein each letter in an alphabet is mapped to its numeric
    equivalent, encrypted using a simple mathematical function, and 
    converted back to a letter. Each letter is enciphered with the 
    function (ax + b) mod 26, where b is the magnitude of the shift.
    """


    #defines initial aplphabet
    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.mod26 = {letter: number for letter,
                      number in zip([item for item in self.alphabet],
                                    [num for num in range(0, 26)])}
        self.mod26_inverse = {number: letter for number,
                              letter in zip([num for num in range(0, 26)],
                                            [item for item in self.alphabet])}
            
    # encryption function E(x)= (ax+b)mod26
    def encrypt(self):
        text = input("What would you like to encrypt?\n>> ").upper()
        proxy_text = [letter for letter in text]
        encrypted_text = []
        
        for letter in proxy_text:
            if letter == ' ':
                encrypted_text.append('')
            else:
                encrypted_text.append(str(self.mod26[letter]))
                
        return ' '.join(encrypted_text)
        
        
    #decryption function D(x) = a^(-1)(x-b)mod26
    def decrypt(self):
        text = input("What would you like to decrypt?\nBe sure to separate \
                     numbers with a space!\n>> ").upper()
        proxy_text = [item for item in text.split(' ')]
        decrypted_text = []
        
        for number in proxy_text:
            if number == ' ':
                decrypted_text.append('')
            else:
                decrypted_text.append(self.mod26_inverse[int(number)])
            
        return ''.join(decrypted_text)
        
