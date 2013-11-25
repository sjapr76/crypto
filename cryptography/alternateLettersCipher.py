# -*- encoding: utf-8 -*-
'''
Created on 23/11/2013

@author: Admin
'''
from cryptography.baseCipher import baseCipher

class alternateLettersCipher(baseCipher):
        
    def encipher(self):
        plain = self.getPlain()
        if plain:
            lar = len(plain)
            res = []
            for i in range(lar/2):
                res.append(plain[i*2])
            for i in range(lar/2):
                res.append(plain[i*2+1])
            if lar % 2 == 1:
                res.append(plain[lar-1])
            ciphered = "".join(res)
            self.setCiphered(ciphered)
            print "Plain text: " + self.getPlain()
            print "Ciphered as: " + ciphered
        else:
            print "Set plain text. Use setPlain(text) function."
        
    def decipher(self):
        ciphered = self.getCiphered()
        if ciphered:
            lar = len(ciphered)
            res = []
            for i in range(lar/2):
                res.append(ciphered[i])
                res.append(ciphered[(lar/2+i)])
            if lar % 2 == 1:
                res.append(ciphered[lar-1])
            plain = "".join(res)
            self.setPlain(plain)
            print "Ciphered text: " + self.getCiphered()
            print "Deciphered as: " + plain
        else:
            print "Set ciphered text. Use setCiphered(text) function."

if __name__ == "__main__":
    print "Test Encipher..."
    cipher = alternateLettersCipher(plain="Este texto esta cifrado.")
    cipher.encipher()
    print "\nTest Decipher..."
    cipher = alternateLettersCipher(ciphered="Et et sacfaosetxoet ird.")
    cipher.decipher()