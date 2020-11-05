import time
import sympy
from sympy.crypto.crypto import decipher_rsa, encipher_rsa
from sympy.crypto.crypto import rsa_public_key, rsa_private_key

def get_d(e,z):
    l = [z]
    m = [e]
    f = [z // e]
    r = z % e
    count = 0

    while r != 0:
        count += 1
        l.append(m[-1])
        m.append(r)
        f.append(l[-1] // m[-1])
        r = l[-1] % r
    if m[-1] != 1:
        print("ggT not 1")
        return
    u = 1
    v = -f[-2]
    pos = len(l) - 3

    while pos >= 0:
        tmp = u
        u = v
        v = tmp - v * f[pos]
        pos = pos - 1

    if v < 0:
        return z + v
    else:
        return v

def createKey():
    p = sympy.randprime(1E7, 1E8)
    q = sympy.randprime(1E7, 1E8)
    n = p * q
    z = (p-1)*(q-1)
    e = sympy.randprime(2, z) 
    d = get_d(e, z)
    private_key = rsa_private_key(n, d)
    public_key = rsa_public_key(n, e)

    return private_key, public_key


def encrypt(msg, public_key):
    ascii_msg = [ord(c) for c in msg]
    
    for ascii_msg in len(ascii_msg): 
        enc_msg = encipher_rsa(ascii_msg, public_key)
    
    return enc_msg


def decrypt(msg, private_key):
    dec_msg = decipher_rsa(msg, private_key)

    return dec_msg

if __name__ == "__main__":
    private_key, public_key = createKey()
    print(encrypt("Hallo", public_key))
    
