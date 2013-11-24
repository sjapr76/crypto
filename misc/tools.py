'''
Created on 24/11/2013

@author: Admin
'''

from cryptography.baseCipher import alpha_upper


def createShiftedAlphabet(number):
    lar = len(alpha_upper)
    return "".join([alpha_upper[i+number]\
                            if i+number <= lar-1 else alpha_upper[i+number-lar] \
                            for i in range(lar)])


def getMatrixAlphabet():
    matrixAlphabet = {}
    for j in range(len(alpha_upper)):
        matrixAlphabet[alpha_upper[j]] = createShiftedAlphabet(j)
    print matrixAlphabet
    

getMatrixAlphabet() 