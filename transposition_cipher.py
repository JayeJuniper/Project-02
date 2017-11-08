from ciphers import Cipher


class Transposition(Cipher):
    """In cryptography, a transposition cipher is a method of 
    encryption by which the positions held by units of plaintext (which
    are commonly characters or groups of characters) are shifted 
    according to a regular system, so that the ciphertext constitutes a
    permutation of the plaintext. 
    """


    #defines initial aplphabet
    def __init__(self):
        pass
    
                 
    # Encryption function modeled after the rail fence cipher using 
    # 3 rails.
    def encrypt(self):
        text = input("what would you like to encrypt?\n>> ").upper()              
        proxy1 = text.replace(" ", "")
        proxy2 = ''.join(proxy1[0::4]+proxy1[1::2]+proxy1[2::4])
        encrypted_text = ' '.join(proxy2[i:i+5] for i in range(0,len(proxy2), 
                                                               5))
        
        return encrypted_text
        
        
    #decryption function
    def decrypt(self):
        text = input("what would you like to decrypt?\n>> ").upper()
        proxy1 = text.replace(" ", "")
        
        # Here we reverse engineer the rails used to encode. since the 
        # length of the text is unaltered, the perameters used to create
        # the rails can be used again here so long as this script was 
        # used to encode  
        rail1 = [item for item in proxy1[0:len(proxy1[0::4]):]]
        rail2= [item for item in proxy1[len(proxy1[0::4]):len(proxy1[0::4])
                                        + len(proxy1[1::2]):]]
        rail3 = [item for item in proxy1[len(proxy1[0::4])
                                         + len(proxy1[1::2])::]]        
        decrypted_text = ['.' for item in proxy1]
               
        offset = 0
        for item in rail1:
            decrypted_text[offset] = item
            offset += 4
                        
        offset = 1
        for item in rail2:
            decrypted_text[offset] = item
            offset += 2
            
        offset = 2
        for item in rail3:
            decrypted_text[offset] = item
            offset += 4
            
        return ''.join(decrypted_text)
        
