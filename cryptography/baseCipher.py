# -*- encoding: utf-8 -*-
'''
Created on 23/11/2013

@author: Admin
'''

alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "".join([letter.upper() for letter in alpha_lower])

reversed_alpha_lower = "".join([letter for letter in reversed(alpha_lower)])
reversed_alpha_upper = "".join([letter.upper() for letter in reversed_alpha_lower])

stressedVowelTranslate = {"Á":"A",
                          "É":"E",
                          "Í":"I",
                          "Ó":"O",
                          "Ú":"U",
                          "á":"a",
                          "é":"e",
                          "í":"i",
                          "ó":"o",
                          "ú":"u"}

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

    def removeDuplicates(self,alph):
        newAlph = []
        for c in alph:
            if c not in newAlph:
                newAlph.append(c)
        return "".join(newAlph)
        
    def alphaToDict(self, alph, reverse=None):
        if reverse:
            #pos as key, letter as value
            return dict([[i,x] for i, x in enumerate(alph)])
        else:
            #letter as key, pos as value
            return dict([[x,i] for i, x in enumerate(alph)])
        
    def translateVowel(self, vowela):
        return stressedVowelTranslate[vowela]
        
if __name__ == "__main__":
    baseCipher()