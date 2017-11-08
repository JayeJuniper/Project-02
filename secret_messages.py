import os
import sys

from caesar_cipher import Caesar
from keyword_cipher import Keyword
from affine_cipher import Affine
from transposition_cipher import Transposition


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def welcome():
    """Enables the user to select a cipher and either encrypt or 
    decrypt a message. Once complete the encrypted/decrypted message
    will be returned, and the user will be prompted to restart or quit.    
    """
    
    clear()
    cipher_choice = None
    encrypt_or_decrypt = None
    cipher_dict = {
        '1': 'Caesar',
        '2': 'Keyword',
        '3': 'Affine',
        '4': 'Transposition'
    }
        
    print("""Welcome to the Secret Messages project for treehouse techdegree.
    Select a cipher from the list below or press 'q' to quit:\n
    1 - Caesar
    2 - Keyword
    3 - Affine 
    4 - Transposition
    """
         )
    
    # Select cipher type.
    while cipher_choice == None:        
        cipher_choice = input("Enter 1, 2, 3, or 4 to begin.\n>> ").lower()
        if cipher_choice not in ['1', '2', '3', '4']:
            if cipher_choice == 'q':
                print("Good Bye.")
                sys.exit()
            else:
                print("Invalid selection, Try again.")
                cipher_choice = None
                
    print("You have selected {}.".format(cipher_dict[cipher_choice]))
        
    # Select Encryption or decryption.
    while encrypt_or_decrypt == None:       
        encrypt_or_decrypt = input("""Would you like to encrypt or decrypt?
>> """
                                  ).lower()
        if encrypt_or_decrypt not in ['encrypt', 'decrypt']:
            if encrypt_or_decrypt == 'q':
                print("Good Bye.")
                sys.exit()
            else:
                print("Invalid selection, Try again.")
                encrypt_or_decrypt = None
                
    # Prints Caesar encryption/decrytion.           
    clear()
    if cipher_choice == '1':        
        if encrypt_or_decrypt == 'encrypt':
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Caesar().encrypt()))
        else:
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Caesar().decrypt()))
            
    # Prints Keyword encryption/decrytion.
    if cipher_choice == '2':
        if encrypt_or_decrypt == 'encrypt':
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Keyword().encrypt()))
        else:
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Keyword().decrypt()))
            
    # Prints Affine encryption/decrytion.
    if cipher_choice == '3':
        if encrypt_or_decrypt == 'encrypt':
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Affine().encrypt()))
        else:
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Affine().decrypt()))
            
    # Prints Transposition encryption/decrytion.
    if cipher_choice == '4':
        if encrypt_or_decrypt == 'encrypt':
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Transposition().encrypt()))
        else:
            print("The {}ed message is: {}".format(encrypt_or_decrypt, 
                                                   Transposition().decrypt()))
    
    # Ask user to restart or quit.
    restart = input(""""Would you like to encrypt/decrypt another message? Y/n
>> """
                   ).upper()
    if restart == 'Y':
        welcome()
    else:
        print("Good Bye.")
        sys.exit()
        
        
if __name__ == "__main__":    
    welcome()
