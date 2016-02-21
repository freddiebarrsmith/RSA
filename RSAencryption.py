
from fractions import gcd
import math
#TODO: Import all discovered primes and randomly select
#Substitute any pair of primes into p or q, m is the message to be encrypted.

p = 131
q = 151
s = ""
s2 = ""

letterarray = []
encryptedarray = []
decryptedarray = []
print "Plaintext:"
messagestring = "testing"
print messagestring

#Get ASCII representation of each character
for letter in messagestring:
        ordletter = ord(letter)
        letterarray.append(ordletter)

# Calculating n which is just p multiplied by q
def ncalculate(p, q):
        n = p * q
        return n



n = ncalculate(p, q)

#Calculating phi which is thankfully just (p-1) x (q-1)

def phicalculate(p, q):
        phelper = p - 1
        qhelper = q - 1
        phi = phelper * qhelper
        return phi
phi = phicalculate(p, q)

#Calculating exponent, which is highest relative prime between 1 and phi

def exponentcalculator(phi):
    for e in xrange(2,phi):
        if gcd(e,phi) == 1 :
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


# Encryption algorithm which multiplies the plaintext (m) to the power of the exponent, then divided by n

def encryptionalgo(m, d, e, phi):

    cipher1 = pow(m, e)
    cipher2 = cipher1 % n

    return cipher2

# Decryption algorithm which times ciphertext by the modular inverse of d and phi


def decryptionalgo(d, e, phi, cipher2):
    cipher3 = pow(cipher2, d)
    cipher4 = cipher3 % n

    return cipher4

#This is where the encryption happens

for letter in letterarray:
    plaintext = letter
    cipher2 = encryptionalgo(plaintext, d, e, phi)
    encryptedarray.append(cipher2)

#This is where the decryption happens

for encryptedletter in encryptedarray:
    decryptionoutput = decryptionalgo(d, e, phi, encryptedletter)
    decryptedarray.append(int(decryptionoutput))


for letter2 in encryptedarray:

    s2 += str(letter2)

print "Encrypted Ciphertext:"
print s2

for letter2 in decryptedarray:
    string = chr(letter2)
    s += str(string)

print "Decrypted Plaintext:"
print s