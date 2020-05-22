from PrivateKey import *
from Ciphertext import *


m1=[]
def decrypt(c,d,N):
    for i in c:
        t= (i**d) % N
        m1.append(t)

    return (m1)

def to_message(m2):
    s=''
    for i in range(len(m2)-1,-1,-1):
        
        n=m2[i]
        while n!=0:
            t2=n%1000
            n=n//1000
            ch=chr(t2)
            s=ch + s
    return s
