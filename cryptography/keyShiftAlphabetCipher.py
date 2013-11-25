'''
Created on 23/11/2013

@author: Admin
'''

from cryptography.alphabetCipher import alphabetCipher
from cryptography.baseCipher import alpha_upper, alpha_lower
from misc.tools import removeDuplicates, alphaToDict

class keyShiftAlphabetCipher(alphabetCipher):
    def __init__(self, plain=None, ciphered=None, key=None):
        self._shiftedAlphabet = None
        if self.keyIsString(key.upper()):
            self._key = "".join(removeDuplicates(key.upper()))
            self.createShiftedAlphabet(self._key)
            alphabetCipher.__init__(self, plain, ciphered, self._shiftedAlphabet)
        else:
            self._key = None
            self._plain = plain
            self._ciphered = ciphered
            print "\nYou must set a string as key.\nUse the function setKey(string).\n"
            
    def keyIsString(self, key):
        if key:
            for c in key:
                if c not in alpha_upper:
                    return False
            return True
        else:
            return False
            
    def setKey(self,key):
        if self.keyIsString(key.upper()):
            self._key = "".join(removeDuplicates(key.upper()))
            self.createShiftedAlphabet(self._key)
            alphabetCipher.__init__(self, self._plain, self._ciphered, self._shiftedAlphabet)
        else:
            print "\nYou must set a string as key.\n"
    
    def getShift(self):
        return self._shift
            
    def createShiftedAlphabet(self, key):
        res = list(alpha_upper)
        for letter in key:
            if letter in key: 
                res.remove(letter)
        res = "".join(res)
        nextPos = alphaToDict(alpha_upper)[key[len(key) - 1]] + 1
        nextLetter = alphaToDict(alpha_upper,reverse=True)[nextPos]
        firstPos = alphaToDict(res)[nextLetter]
        lar = len(res)
        rest_alph = "".join([res[i+firstPos]\
                    if i+firstPos <= lar - 1 else res[i+firstPos-lar] \
                    for i in range(lar)])

        self._shiftedAlphabet = key + rest_alph

if __name__ == "__main__":
    print "Test Encipher..."
    cipher = keyShiftAlphabetCipher(plain="Este texto esta cifrado.",key="HOLACOMOESTAS")
    cipher.encipher()
    print "\nTest Decipher..."
    cipher = keyShiftAlphabetCipher(ciphered="CGICICPIZCGIHLTMFHAZ",key="HOLACOMOESTAS")
    cipher.decipher()