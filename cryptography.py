"""
cryptography.py
Author: James Napier
Credit: 

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
input1=""
while input1 != "q":
    input1=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    inputr=input1.lower()
    if inputr == "e":
        msg_in=input("Message: ")
        key_in=input("Key: ")
        key_ina=key_in*(len(msg_in)//len(key_in)+1)
        msg_a=[associations.find(x) for x in msg_in]
        key_a=[associations.find(y) for y in key_ina]
        m_k_a=zip(msg_a, key_a)
        comp_nums=list(z[0] + z[1] for z in m_k_a)
        for n, c in enumerate(comp_nums):
            if c >= 85:
                c= c-85
            else:
                c=c
            comp_nums[n] = c
        enclist = [associations[u] for u in comp_nums]
        fin=("".join(enclist))
        print(fin)
    elif inputr == "d":
        msg_in2=input("Message: ")
        key_in2=input("Key: ")
        key_inz=key_in2*(len(msg_in2)//len(key_in2)+1)
        msg_az=[associations.find(p) for p in msg_in2]
        key_az=[associations.find(m) for m in key_inz]
        mkz=zip(msg_az, key_az)
        comp_numsz=list(z[0] - z[1] for z in mkz)
        enclistz = [associations[q] for q in comp_numsz]
        print(''.join(enclistz))
    elif inputr == "q":
        print("Goodbye!")
    elif inputr != "q" and inputr != "e" and inputr !="d" and inputr !="e":
        print("Did not understand command, try again.")
        
        
        
        
    
        
        
       