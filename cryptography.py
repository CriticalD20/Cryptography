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
    for n, c in enumerate(comp_nums):
        if c > 77:
            c= c-78
        else:
            c=c
        comp_nums[n] = c
    enclist = [associations[c] for c in comp_nums]
    print(''.join(enclist))
    continue
            
elif inputr == "d":
    msg_in2=("Message: ")
    key_in2=("Key: ")
    key_in=key_in*(len(msg_in)//len(key_in)+1)
    msg_a=[associations.find(x) for x in msg_in]
    key_a=[associations.find(y) for y in key_in]
    m_k_a=zip(msg_a, key_a)
    mk_a=[(t[0]+t[1]) for t in m_k_a]
    mkz=zip(mk_a, key_a)
    comp_nums=list(z[0] + z[1] for z in mkz)
    enclist = [associations[z] for z in comp_nums]
    print(''.join(enclist))
    continue
elif inputr == "q":
    print("Goodbye!")
     
elif inputr != "q" and inputr != "e" and inputr !="d" and inputr !="e":
    print("Did not understand command, try again.")
    continue