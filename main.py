import math, numpy

"""apply Blum Goldwasser Probabilistic Algorithm (encryption) to the specified message
@param m: the message to encrypt
@param p: 
@param a: 
@param b: 
@param x0: 
@returns: the result of encrypting the specified message with the specified parameters using the Blum Goldwasser algorithm
"""
def BGPEnc(m,p=499,q=547,a=-57,b=52,x0=159201):
    n=p*q
    k = int(numpy.log2(n))
    h = int(numpy.log2(k))
    t = len(m)//h
    
    mts = [m[i*h:i*h+h] for i in range(t)]
    c = []
    for m in mts:
        x0 = pow(x0, 2, n)
        pi = str(bin(x0))[-h:]
        for i in range(h):
            c.append(1 if pi[i] != str(m[i]) else 0)
    return c,pow(x0, 2, n)

def gcd(x,y):
    smaller = y if x > y else x
    for i in range(1, smaller+1): 
        if((x % i == 0) and (y % i == 0)): 
            g = i 
    return g

"""apply Blum Goldwasser Probabilistic Algorithm (decryption) to the specified message
@param m: the message to encrypt
@param p: 
@param a: 
@param b: 
@param x0: 
@returns: the result of decrypting the specified message with the specified parameters using the Blum Goldwasser algorithm
"""
def BGPDec(m,x,p=499,q=547,a=-57,b=52,x0=159201):
    n=p*q
    k = int(numpy.log2(n))
    h = int(numpy.log2(k))
    t = len(m)//h
    
    d1 = pow(((p+1)//4), t+1, p-1)
    d2 = pow(((q+1)//4), t+1, q-1)
    u = pow(x, d1, p)
    v = pow(x, d2, q)
    x = (v*a*p + u*b*q) % n
    
    mts = [m[i*h:i*h+h] for i in range(t)]
    c = []
    for m in mts:
        x0 = pow(x0, 2, n)
        pi = str(bin(x0))[-h:]
        for i in range(h):
            c.append(1 if pi[i] != str(m[i]) else 0)
    return c
    

def main():
    m=[1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0]
    enc,x0 = BGPEnc(m)
    dec = BGPDec(enc,x0)
    print("  message: {0}\nencrypted: {1}\ndecrypted: {2}\noriginal = decrypted? {3}".format(m,enc,dec,m==dec))
    

if __name__ == "__main__":
    main()