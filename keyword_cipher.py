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


    # Defines initial aplphabet
    def __init__(self):
        self.alphabet = string.ascii_uppercase
        
        
    # Creates a new alphabet using keyword given by user
    def __alphabet_generation(self, key_actual):
        proxy1_alphabet = list(self.alphabet)
        for item in key_actual:
            if item in proxy1_alphabet:
                proxy1_alphabet.remove(item)
        proxy2_alphabet = ''.join(key_actual) + ''.join(proxy1_alphabet)
        return proxy2_alphabet
           
            
    # Will take user defined key and remove all duplicate letters
    def __key_generation(self, items):
        actual = []
        for item in items:
            if item not in actual:
                actual.append(item)
        return actual
    
    
    # encryption function
    def encrypt(self):
        text = input("What would you like to encrypt?\n>> ").upper()
                
        # Ask for key the cipher will use and set as uppercase list 
        # before sending to key generation.
        key_user = list(input("Type the key you wish to use for the cipher.\
                              \n>> ").upper())
        key_actual = self.__key_generation(key_user)     
                
        # new alphabet based on user defined key
        new_alphabet = self.__alphabet_generation(key_actual)
                
        # encryption actual
        # list of ords - 65 for alphabet indexes
        Proxy_text = [(ord(x) - 65) for x in text]
        # Add spaces and replace with the letter of the new_alphabet
        encrypted_text = ''.join([(" " if x < 0 else (new_alphabet[x])) for 
                                  x in Proxy_text])
        
        return encrypted_text
        

    #decryption function
    def decrypt(self):
        text = input("What would you like to decrypt?\n>> ").upper()
        
        # Ask for key the cipher will use and set as uppercase list 
        # before sending to key generation.
        key_user = list(input("""Type the key you wish to use for the cipher.
                              >> """
                             ).upper())
        key_actual = self.__key_generation(key_user)     
                
        # new alphabet based on user defined key
        new_alphabet = self.__alphabet_generation(key_actual) 
        
        # Add a space if tehre is a space in text and adding index
        # of letters given.
        proxy_text = [(new_alphabet.index(x) if x in new_alphabet else " ") 
                      for x in text]
        # Add spaces, replacing new_alphabet indexing with 
        # self.alphabet indexing to return decrypted text
        decrypted_text = ''.join([(" " if x == " " else (self.alphabet[x])) 
                                  for x in proxy_text])
        
        return decrypted_text          
        
