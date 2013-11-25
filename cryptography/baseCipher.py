# -*- encoding: utf-8 -*-
'''
Created on 23/11/2013

@author: Admin
'''

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