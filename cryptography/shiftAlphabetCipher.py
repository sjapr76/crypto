'''
Created on 23/11/2013

@author: Admin
'''

from cryptography.alphabetCipher import alphabetCipher
from cryptography.baseCipher import alpha_upper, alpha_lower

class shiftAlphabetCipher(alphabetCipher):
    def __init__(self, plain=None, ciphered=None, shift=None):
        nshift = unicode(shift)
        self._shiftedAlphabet = None
        if nshift.isnumeric():
            self._shift = int(nshift)
            self.createShiftedAlphabet(self._shift)
            alphabetCipher.__init__(self, plain, ciphered, self._shiftedAlphabet)
        else:
            self._plain = plain
            self._ciphered = ciphered
            self._shift = None
            print "\nYou must set the number of places to shift.\nUse the function setShift(number).\n"
            
    def setShift(self,number):
        nshift = unicode(number)
        if nshift.isnumeric():
            self._shift = int(nshift)
            self.createShiftedAlphabet(self._shift)
            alphabetCipher.__init__(self, self._plain, self._ciphered, self._shiftedAlphabet)
        else:
            print "\nYou must set the number of places to shift.\n"
    
    def getShift(self):
        return self._shift
            
    def createShiftedAlphabet(self, number):
        lar = len(alpha_upper)
        self._shiftedAlphabet = "".join([alpha_upper[i+number]\
                                if i+number <= lar-1 else alpha_upper[i+number-lar] \
                                for i in range(lar)])

if __name__ == "__main__":
    print "Test Encipher..."
    cipher = shiftAlphabetCipher(plain="Este texto esta cifrado.",shift=5)
    cipher.encipher()
    print "\nTest Decipher..."
    cipher = shiftAlphabetCipher(ciphered="JXYJYJCYTJXYFHNKWFIT",shift=5)
    cipher.decipher()