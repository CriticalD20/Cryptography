"""
cryptography.py
Author: James Napier
Credit: 

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
input1=input("Enter e to encrypt, d to decrypt, or q to quit: ")
inputr=input1.lower()


x=1
if x >= 0:
    if inputr == "e":
        msg_in=input("Message: ")
        key_in=input("Key: ")
        for L in msg_in:
            associations.index(L)
            listas=list(associations.index(L))
                for i in listas
                
    elif inputr == "d":
        msg_in2=("Message: ")
        key_in2=("Key: ")
     
    elif inputr == "q":
        print("Goodbye!")
     
    else:
        print("Did not understand command, try again.")
