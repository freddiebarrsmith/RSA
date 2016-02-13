from fractions import gcd
import math
#Substitute any pair of primes into p or q, m is the message to be encrypted. 
#TODO: plaintextencoder can be used to change plaintext into a numerical representation. 

p = 131
q = 151
m = 2
#messagestring = ""
#def plaintextencoder(m):
#    for letter in messagestring:
#        print letter
#    return None

def ncalculate(p, q):
        n = p * q
        return n



n = ncalculate(p, q)
print n
def phicalculate(p, q):
        phelper = p - 1
        qhelper = q - 1
        phi = phelper * qhelper
        return phi
phi = phicalculate(p, q)
print phi


def exponentcalculator(phi):
    for e in xrange(2,phi):
        if gcd(e,phi) == 1 :
           print e
           return e
           break
        else:
           continue

e = exponentcalculator(phi)
#e = 7

#d = 3
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

d =  modinv(e, phi)
print "d:"
print d

def encryptionalgo(m, d, e, phi):
    print m
    print d
    print e
    cipher1 = pow(m, e)
    cipher2 = cipher1 % n
    print "ciphertext"
    print cipher2
    return cipher2

cipher2 = encryptionalgo(m, d, e, phi)
def decryptionalgo(m, d, e, phi, cipher2):
    cipher3 = pow(cipher2, d)
    cipher4 = cipher3 % n
    print "decrypted"
    print cipher4

decryptionalgo(m, d, e, phi, cipher2)
