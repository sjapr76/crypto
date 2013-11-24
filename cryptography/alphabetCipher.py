'''
Created on 23/11/2013

@author: Admin
'''

from cryptography.baseCipher import baseCipher
from cryptography.baseCipher import alpha_upper, alpha_lower

class alphabetCipher(baseCipher):
    
    def __init__(self, plain=None, ciphered=None, alphabet=None):
        baseCipher.__init__(self, plain, ciphered)
        if alphabet:
            new_alphabet = self.removeDuplicates(alphabet)
            if len(new_alphabet) == 26:
                self._alphabet = str(new_alphabet).upper()
                print "Original Alphabet: " + alpha_lower
                print "Cipher Alphabet:   " + self._alphabet
            else:
                print "\nYou must set a 26 characters alphabet.\nUse the function setAlphabet(alphabet).\n"
        else:
            print "\nYou must set a 26 characters alphabet.\nUse the function setAlphabet(alphabet).\n"
    
    def removeDuplicates(self,alph):
        newAlph = []
        for c in alph:
            if c not in newAlph:
                newAlph.append(c)
        return "".join(newAlph)
    
    def setAlphabet(self, alph):
        new_alphabet = self.removeDuplicates(alph)
        if len(new_alphabet) == 26:
            self._alphabet = str(new_alphabet).upper()
        else:
            print "\nYou must set a 26 characters alphabet.\n"
        
    def getAlphabet(self):
        return self._alphabet
        
    def alphaToDict(self, alph, reverse=None):
        if reverse:
            return dict([[i,x] for i, x in enumerate(alph)])
        else:
            return dict([[x,i] for i, x in enumerate(alph)])
        
    def encipher(self):
        alph = self.getAlphabet()
        plain = self.getPlain()
        if alph and plain:
            alphaDict = self.alphaToDict(alpha_lower)
            res = []
            for character in plain:
                try:
                    res.append(alph[alphaDict[character.lower()]])
                except Exception:
                    res.append(character)
            ciphered = "".join(res)
            self.setCiphered(ciphered)
            print "Plain text: " + plain
            print "Ciphered as: " + ciphered
        else:
            print "\nYou must set a 26 characters alphabet.\nUse the function setAlphabet(alphabet).\nSet plain text. Use setPlain(text) function.\n"
    
    def decipher(self):
        alph = self.getAlphabet()
        ciphered = self.getCiphered()
        if alph and ciphered:
            alphaDict = self.alphaToDict(alph)
            res = []
            for character in ciphered:
                try:
                    res.append(alpha_lower[alphaDict[character.upper()]])
                except Exception:
                    res.append(character)
            plain = "".join(res)
            self.setPlain(plain)
            print "Ciphered text: " + ciphered
            print "Deciphered as: " + plain
        else:
            print "\nYou must set a 26 characters alphabet.\nUse the function setAlphabet(alphabet).\nSet plain text. Use setCiphered(text) function.\n"
            
monoAlphabetCipher = alphabetCipher

if __name__ == "__main__":
    print "Test Encipher..."
    cipher = monoAlphabetCipher(plain="Este texto esta cifrado.",alphabet="qwertyuiopasdfghjklzxcvbnm")
    cipher.encipher()
    print "\nTest Decipher..."
    cipher = monoAlphabetCipher(ciphered="TLZT ZTBZG TLZQ EOYKQRG",alphabet="qwertyuiopasdfghjklzxcvbnm")
    cipher.decipher()