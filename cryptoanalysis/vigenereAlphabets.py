'''
Created on 24/11/2013

@author: Admin
'''

def getLettersByPosition(ciphered, pos, size):
    lar = (len(ciphered) / size) + 1
    res = []
    for i in range(lar):
        if (pos+i*size) < len(ciphered):
            res.append(ciphered[pos+i*size])
    return "".join(res)

def getLettersByNumberOfAlphabet(ciphered, size):
    distributedCiphered = {}
    for i in range(size):
        distributedCiphered[i] = getLettersByPosition(ciphered,i,size)
    return distributedCiphered