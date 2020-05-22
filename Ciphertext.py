# convert message into numbers
from Modular import *


class Ciphertext:

    def to_num(s, N):

        m = []
        num = 0
        
        # convert every character to its ascii value
        for i in range(len(s)):
            x=s[i]
            if num*100 <= N:
                
                ascii_val = ord(x)
                num = num*1000 + ascii_val
                
            else:

                # Split, append to list
                m.append(num)
                num = 0
                ascii_val = ord(x)
                num = num*1000 + ascii_val

            if i==(len(s)-1):
                m.append(num)

        return m

    def generate_ciphertext(m,N,E): 

        c=[]
        for i in m:
            
            #DEVELOP CIPHER TEXT

            t = (i**E)%N
            c.append(t)
        return c
