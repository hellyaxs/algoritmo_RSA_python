import random

def totient(number): 
    if(prime(number)):
        return number-1
    else:
        return False


def prime(n): # verica se um numero e primo
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True

def generate_E(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e

def generate_prime(): # generate the prime number - p e 
    while True: # 2**2048 is the RSA standart keys
        x=random.randrange(1,100) # define the range of 
        if(prime(x)==True):
            return x

def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c

def cipher(words,e,n): # get the words and compute the cipher
    tam = len(words)
    i = 0
    lista = []
    while(i < tam):
        letter = words[i]
        k = ord(letter)
        k = k**e
        d = mod(k,n)
        lista.append(str(d))
        i += 1
    return lista


def descifra(cifra,n,d):
    lista = ""
    i = 0
    tamanho = len(cifra)
    # texto=cifra ^ d mod n
    while i < tamanho:
        result = int(cifra[i])**d
        texto = mod(result,n)
        letra = chr(texto)
        lista = lista+letra
        i += 1
    return lista

def calculate_private_key(toti,e):
    d = 0
    while(mod(d*e,toti)!=1):
        d += 1
    return d

