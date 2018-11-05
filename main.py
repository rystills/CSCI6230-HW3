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
    mts = []
    for i in range(0,t):
        mts.append(m[i*h:i*h+h])
    #print(mts)
    c = []
    for m in mts:
        x0 = pow(x0, 2, n)
        pi = str(bin(x0))[-h:]
        #print("pi:",pi)
        for i in range(h):
            c.append(1 if pi[i] != str(m[i]) else 0)
    return c

"""apply Blum Goldwasser Probabilistic Algorithm (decryption) to the specified message
@param m: the message to encrypt
@param p: 
@param a: 
@param b: 
@param x0: 
@returns: the result of decrypting the specified message with the specified parameters using the Blum Goldwasser algorithm
"""
def BGPDec(m,x,t,p=499,q=547,a=-57,b=52,x0=159201):
    return m


def main():
    #store message in binary (lists were causing more trouble than they were worth)
    m=[1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0]
    #m="10011100000100001100"
    #m=int('10011100000100001100', 2)
    enc = BGPEnc(m)
    #print("  message: {0}\nencrypted: {1}".format(bin(m),bin(enc[0])))
    print("  message: {0}\nencrypted: {1}".format(m,enc))
    

if __name__ == "__main__":
    main()