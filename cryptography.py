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


if inputr == "e":
    msg_in=input("Message: ")
    key_in=input("Key: ")
    key_in=key_in*(len(msg_in)//len(key_in)+1)
    msg_a=[associations.find(x) for x in msg_in]
    key_a=[associations.find(y) for y in key_in]
    m_k_a=zip(msg_a, key_a)
    comp_nums=list(z[0] + z[1] for z in m_k_a)
    print(associations[index] for c in comp_nums)
    #find out why there is an error in the line above/how to index from a list
    
        
            
            
                
elif inputr == "d":
    msg_in2=("Message: ")
    key_in2=("Key: ")
     
elif inputr == "q":
    print("Goodbye!")
     
else:
    print("Did not understand command, try again.")
