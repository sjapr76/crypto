# -*- encoding: utf-8 -*-
'''
Created on 25/11/2013

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