'''
Created on 23/11/2013

@author: Admin
'''

from cryptography.alphabetCipher import baseCipher
from cryptography.baseCipher import alpha_upper, alpha_lower

matrixAlphabet = {'A': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                  'B': 'BCDEFGHIJKLMNOPQRSTUVWXYZA',
                  'C': 'CDEFGHIJKLMNOPQRSTUVWXYZAB', 
                  'D': 'DEFGHIJKLMNOPQRSTUVWXYZABC',
                  'E': 'EFGHIJKLMNOPQRSTUVWXYZABCD', 
                  'F': 'FGHIJKLMNOPQRSTUVWXYZABCDE', 
                  'G': 'GHIJKLMNOPQRSTUVWXYZABCDEF', 
                  'H': 'HIJKLMNOPQRSTUVWXYZABCDEFG', 
                  'I': 'IJKLMNOPQRSTUVWXYZABCDEFGH', 
                  'J': 'JKLMNOPQRSTUVWXYZABCDEFGHI', 
                  'K': 'KLMNOPQRSTUVWXYZABCDEFGHIJ', 
                  'L': 'LMNOPQRSTUVWXYZABCDEFGHIJK', 
                  'M': 'MNOPQRSTUVWXYZABCDEFGHIJKL', 
                  'N': 'NOPQRSTUVWXYZABCDEFGHIJKLM', 
                  'O': 'OPQRSTUVWXYZABCDEFGHIJKLMN', 
                  'P': 'PQRSTUVWXYZABCDEFGHIJKLMNO', 
                  'Q': 'QRSTUVWXYZABCDEFGHIJKLMNOP', 
                  'R': 'RSTUVWXYZABCDEFGHIJKLMNOPQ', 
                  'S': 'STUVWXYZABCDEFGHIJKLMNOPQR', 
                  'T': 'TUVWXYZABCDEFGHIJKLMNOPQRS', 
                  'U': 'UVWXYZABCDEFGHIJKLMNOPQRST', 
                  'V': 'VWXYZABCDEFGHIJKLMNOPQRSTU', 
                  'W': 'WXYZABCDEFGHIJKLMNOPQRSTUV', 
                  'X': 'XYZABCDEFGHIJKLMNOPQRSTUVW', 
                  'Y': 'YZABCDEFGHIJKLMNOPQRSTUVWX', 
                  'Z': 'ZABCDEFGHIJKLMNOPQRSTUVWXY'}


class vigenereCipher(baseCipher):
    def __init__(self, plain=None, ciphered=None, key=None):
        self._repeatedKey = None
        if self.keyIsString(key.upper()):
            self._key = key.upper()
            baseCipher.__init__(self, plain, ciphered)
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
            self._key = key.upper()
            baseCipher.__init__(self, self._plain, self._ciphered)
            self.createRepeatedKey(self._key)
        else:
            print "\nYou must set a string as key.\n"
            
    def createRepeatedKey(self, key, text):
        if text:
            repeatedKey = ""
            lar = len(text)
            while len(repeatedKey)+len(key) <= lar:
                repeatedKey += key
            if len(repeatedKey) < lar:
                over = len(repeatedKey)+len(key) - lar
                repeatedKey += key[0:len(key)-over]
            self._repeatedKey = repeatedKey
        else:
            "\nYou must set the text to encipher or decipher.\n"
    
    def generateAlphabets(self, key, reverse=False):
        alphaDict = {}
        for letter in key:
            if reverse:
                alphaDict[letter] = self.alphaToDict(matrixAlphabet[letter],reverse=True)
            else:
                alphaDict[letter] = self.alphaToDict(matrixAlphabet[letter])
        return alphaDict
        
    def _getPlain(self):
        plain = self.getPlain()
        if plain:
            res = []
            for letter in plain.upper():
                if letter in alpha_upper:
                    res.append(letter)
            return "".join(res)
        else:
            return None
    
    def encipher(self):
        plain = self._getPlain()
        if plain:
            alphabetsDict = self.generateAlphabets(self._key, reverse=True)
            self.createRepeatedKey(self._key, plain)
            alphaDict = self.alphaToDict(alpha_upper)
            res = []
            count = 0
            for character in plain:
                pos = alphaDict[character]
                alphabet = self._repeatedKey[count]
                res.append(alphabetsDict[alphabet][pos])
                count += 1
            ciphered = "".join(res)
            self.setCiphered(ciphered)
            print "Plain text: " + self.getPlain()
            print "Ciphered as: " + ciphered
        else:
            print "\nSet plain text. Use setPlain(text) function.\n"
            
    def decipher(self):
        ciphered = self.getCiphered()
        if ciphered:
            alphabetsDict = self.generateAlphabets(self._key)
            self.createRepeatedKey(self._key, ciphered)
            alphaDict = self.alphaToDict(alpha_upper, reverse=True)
            res = []
            count = 0
            for character in ciphered.upper():
                alphabet = self._repeatedKey[count]
                pos = alphabetsDict[alphabet][character]
                res.append(alphaDict[pos])
                count += 1
            plain = "".join(res)
            self.setPlain(plain)
            print "Ciphered text: " + self.getCiphered()
            print "Deciphered as: " + plain
        else:
            print "\nSet plain text. Use setCiphered(text) function.\n"
 
if __name__ == "__main__":
    print "Test Encipher..."
    cipher = vigenereCipher(plain="Este texto esta cifrado.",key="WHITE")
    cipher.encipher()
    print "\nTest Decipher..."
    cipher = vigenereCipher(ciphered="AZBXXAEBHIOAIVMBYIWS",key="WHITE")
    cipher.decipher()