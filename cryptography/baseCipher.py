'''
Created on 23/11/2013

@author: Admin
'''

alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "".join([letter.upper() for letter in alpha_lower])

reversed_alpha_lower = "".join([letter for letter in reversed(alpha_lower)])
reversed_alpha_upper = "".join([letter.upper() for letter in reversed_alpha_lower])

class baseCipher:
    def __init__(self,plain=None,ciphered=None):
        self._plain = unicode(plain) if plain else plain
        self._ciphered = unicode(ciphered) if ciphered else ciphered
    
    def setPlain(self, plain):
        self._plain = plain
        
    def getPlain(self):
        return self._plain
        
    def setCiphered(self, ciphered):
        self._ciphered = ciphered
        
    def getCiphered(self):
        return self._ciphered

if __name__ == "__main__":
    baseCipher()