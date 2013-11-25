# -*- encoding: utf-8 -*-

'''
Created on 24/11/2013

@author: Admin
'''

def getFrequency(text):
    count = {}
    freq = {}
    lar = len(text)
    for letter in text:
        if letter in count.keys():
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in count.keys():
        freq[letter] = 100*float(count[letter])/float(lar)
    return count, freq
