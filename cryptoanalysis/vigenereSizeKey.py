# -*- encoding: utf-8 -*-
'''
Created on 24/11/2013

@author: Admin
'''

from misc.tools import *

def getVigenereSizeKey(ciphered, rang, filt):
    '''
    Gets the probability of sizes of keys based on rang (min,max) where
    range are the possible sizes of keys.
    Filters the words with lower amount of repetitions than filt, if filt
    is high it is more optimal but it could not be totally accurate.
    '''
    dicts = calculateWordRepetitions(ciphered, rang, filt)
    listFactors = []
    for res in dicts:
        dictSpacing = calculateSpacing(res)
        factors = getFactors(dictSpacing,rang)
        listFactors.append(factors)
    
    factors = summarizeFactors(listFactors)
    sizesOfKey = calculateSizeKeyStatistics(factors)
    print "The probability of sizes of the key are the following: "
    amount = len(sizesOfKey.keys())
    for i in range(amount):
        higher = getHigher(factors)
        print "Size: " + str(higher) + " - Probability: " + str(sizesOfKey[higher]) + "%"
        factors.pop(higher)
