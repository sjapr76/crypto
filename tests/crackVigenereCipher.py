# -*- encoding: utf-8 -*-
'''
Created on 24/11/2013

@author: Admin
'''

from cryptography.vigenereCipher import vigenereCipher
from cryptoanalysis.vigenereSizeKey import getVigenereSizeKey
from cryptoanalysis.vigenereAlphabets import getLettersByNumberOfAlphabet
from cryptoanalysis.frequencyAnalysis import getFrequency

print "Test Encipher..."
cipher = vigenereCipher(plain="""Cryptography (or cryptology; from Greek κρυπτός, "hidden, secret"; and γράφειν, graphein, "writing", or -λογία, -logia, "study", respectively)[1] is the practice and study of techniques for secure communication in the presence of third parties (called adversaries).[2] More generally, it is about constructing and analyzing protocols that overcome the influence of adversaries[3] and which are related to various aspects in information security such as data confidentiality, data integrity, authentication, and non-repudiation.[4] Modern cryptography intersects the disciplines of mathematics, computer science, and electrical engineering. Applications of cryptography include ATM cards, computer passwords, and electronic commerce.
Cryptography prior to the modern age was effectively synonymous with encryption, the conversion of information from a readable state to apparent nonsense. The originator of an encrypted message shared the decoding technique needed to recover the original information only with intended recipients, thereby precluding unwanted persons to do the same. Since World War I and the advent of the computer, the methods used to carry out cryptology have become increasingly complex and its application more widespread.
Modern cryptography is heavily based on mathematical theory and computer science practice; cryptographic algorithms are designed around computational hardness assumptions, making such algorithms hard to break in practice by any adversary. It is theoretically possible to break such a system but it is infeasible to do so by any known practical means. These schemes are therefore termed computationally secure; theoretical advances, e.g., improvements in integer factorization algorithms, and faster computing technology require these solutions to be continually adapted. There exist information-theoretically secure schemes that provably cannot be broken even with unlimited computing power—an example is the one-time pad—but these schemes are more difficult to implement than the best theoretically breakable but computationally secure mechanisms.
Cryptology-related technology has raised a number of legal issues. In the United Kingdom, additions to the Regulation of Investigatory Powers Act 2000 require a suspected criminal to hand over his or her decryption key if asked by law enforcement. Otherwise the user will face a criminal charge.[5] The Electronic Frontier Foundation (EFF) was involved in a case which questioned whether requiring suspected criminals to provide their decryption keys to law enforcement is unconstitutional. The EFF argued that this is a violation of the right of not being forced to incriminate oneself, as given in the fifth amendment.[6]""",key="ESTAESLAK")

print "\nKey: " + cipher.getKey()

cipher.encipher()

ciphered = cipher.getCiphered()

getVigenereSizeKey(ciphered,(3,11),filt=5)

size = 9

distributedText = getLettersByNumberOfAlphabet(ciphered,size)

for i in range(size):
    count,freq = getFrequency(distributedText[i])
    print "\nFrequency Analysis for text related with position " + str(i) + " of the key: "
    print freq

