#class to generate private key
from PublicKey import *
from Modular import *


class PrivateKey:

    def get_keys():

        #collect keys
        l =PublicKey.generate_keys()

        #storing public keys
        N = l[0]
        E = l[1]
        psi=l[2]

        #d is the private key
        d=Modular.modinv(E, psi)

        return [d,N,E]
 
