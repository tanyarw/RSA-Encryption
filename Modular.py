#Class to use modular function


class Modular:
    
    # Iterative Algorithm (xgcd)
    def iterative_egcd(a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q = b // a
            r = b % a
            m = x - u * q
            n = y - v * q  # use x//y for floor "floor division"
            b, a, x, y, u, v = a, r, u, v, m, n
        return b, x, y

    def modinv(a,  m):
            g, x, y = Modular.iterative_egcd(a, m)
            if g != 1:
                return None
            else:
                return x % m

