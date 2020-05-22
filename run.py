from PublicKey import *
from Ciphertext import *
from Decryption import *

l=PrivateKey.get_keys()

#store keys d.N,E individually
d=l[0]
N=l[1]
E=l[2]

s=input("Enter your password: ")
m=Ciphertext.to_num(s,N)

c=Ciphertext.generate_ciphertext(m,N,E)
print("Cihertext:",c)
m1=decrypt(c,d,N)

s=to_message(m1)
print ("Decrypted text:",s)
