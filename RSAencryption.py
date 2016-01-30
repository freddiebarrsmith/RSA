from fractions import gcd
import math
p = 3
q = 11
m = 2

def plaintextencoder(m):
    return None

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

#e = exponentcalculator(phi)
e = 7

#d = 3
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d
d =  multiplicative_inverse(e, phi)
print "d:"
print d

def encryptionalgo(m, d, e, phi):
    print m
    print d
    print e
    cipher1 = math.pow(m, e)
    cipher2 = cipher1 % n
    print "ciphertext"
    print cipher2
    return cipher2

cipher2 = encryptionalgo(m, d, e, phi)
def decryptionalgo(m, d, e, phi, cipher2):
    cipher3 = math.pow(cipher2, d)
    cipher4 = cipher3 % n
    print cipher4

decryptionalgo(m, d, e, phi, cipher2)