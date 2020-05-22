import random
from fractions import gcd

# Generate public key
class PublicKey:

    def __init__(self):
        pass

    def is_prime( x):

        # Corner cases
        if x <= 1:
            return False
        if x <= 3:
            return True

        # This is checked so that we can skip
        # middle five numbers in below loop
        if x % 2 == 0 or x % 3 == 0:
            return False

        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i = i + 6

        return True

    def generate_keys():
        # develop random prime numbers p and q
        p=q=0
        while not PublicKey.is_prime(p):
            p=11
            p = random.randint(1, 1000)  # Since we're developing we're keeping the range small'''
        while not PublicKey.is_prime(q):
            q=3
            q = random.randint(1, 1000)
    
        # Generate public key 1
        N = p*q

        # Generate psi(n)
        psi = (p-1)*(q-1)

        # Generate public key 2
        E = 3

        while gcd(E,psi) != 1:  # n shouldn't be divisible by e
            E = random.randint(1, psi)

        return [N,E,psi]

