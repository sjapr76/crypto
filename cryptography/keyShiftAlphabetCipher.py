'''
Created on 23/11/2013

@author: Admin
'''

from cryptography.alphabetCipher import alphabetCipher
from cryptography.baseCipher import alpha_upper, alpha_lower

class keyShiftAlphabetCipher(alphabetCipher):
    def __init__(self, plain=None, ciphered=None, key=None):
        self._shiftedAlphabet = None
        if self.keyIsString(key):
            self._key = "".join(self.removeDuplicates(key.upper()))
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
        if self.keyIsString(key):
            self._key = "".join(self.removeDuplicates(key.upper()))
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
        nextPos = self.alphaToDict(alpha_upper)[key[len(key) - 1]] + 1
        nextLetter = self.alphaToDict(alpha_upper,reverse=True)[nextPos]
        firstPos = self.alphaToDict(res)[nextLetter]
        lar = len(res)
        rest_alph = "".join([res[i+firstPos]\
                    if i+firstPos <= lar - 1 else res[i+firstPos-lar] \
                    for i in range(lar)])

        self._shiftedAlphabet = key + rest_alph
        print "Original Alphabet: " + alpha_lower
        print "Cipher Alphabet:   " + self._shiftedAlphabet

if __name__ == "__main__":
    print "Test Encipher..."
    cipher = keyShiftAlphabetCipher(plain="Este texto esta cifrado.",key="HOLACOMOESTAS")
    cipher.encipher()
    print "\nTest Decipher..."
    cipher = keyShiftAlphabetCipher(ciphered="CGIC ICPIZ CGIH LTMFHAZ.",key="HOLACOMOESTAS")
    cipher.decipher()