'''
Created on 24/11/2013

@author: Admin
'''

from cryptography.baseCipher import alpha_upper

def getText(text):
    res = []
    for letter in text.upper():
        if letter in alpha_upper:
            res.append(letter)
    return "".join(res)


def createShiftedAlphabet(number):
    lar = len(alpha_upper)
    return "".join([alpha_upper[i+number]\
                            if i+number <= lar-1 else alpha_upper[i+number-lar] \
                            for i in range(lar)])


def getMatrixAlphabet():
    matrixAlphabet = {}
    for j in range(len(alpha_upper)):
        matrixAlphabet[alpha_upper[j]] = createShiftedAlphabet(j)
    print matrixAlphabet
    

def calculateWordRepetitions(text, rang, filt=None):
    '''
    Gets all repeted words in text according to the size
    of words specified in rang.
    Filters the words with lower amount of repetitions than filt
    '''
    #range: range of words size -> tuple = (from, to)
    #filt: minimum number of accepted repetitions, by default 2
    if not filt:
        filt = 2
    res = []
    for i in range(rang[0],rang[1]):
        dictWords = {}
        for j in range(len(text)):
            if j+i <= len(text):
                if text[j:j+i] in dictWords.keys():
                    dictWords[text[j:j+i]].append((j,i))
                else:
                    dictWords[text[j:j+i]] = [(j,i)]
        for key in dictWords.keys():
            if len(dictWords[key]) < filt:
                dictWords.pop(key)
        res.append(dictWords)
    return res


def calculateSpacing(dictWords):
    '''
    dictWords = {word1:repetitions,word2:repetitions}
    repetitions = [(position,len),(position,len)]
    
    Based on the repetitions of each word, calculates
    the spaces between them.
    It returns another dictionary with each word
    and the list of spaces between them.
    
    result = {word1:spaces,word2:spaces}
    spaces = [space,space,space]
    '''
    dictSpacing = {}
    for key in dictWords.keys():
        spaces = []
        repetitions = dictWords[key]
        lar = len(repetitions)
        positions = [pos[0] for pos in repetitions]
        for i in range(lar):
            if i + 1 < lar:
                spaces.append(positions[i+1]-positions[i])
        dictSpacing[key] = spaces
    return dictSpacing

def getFactors(dictSpacing, rang):
    '''
    dictSpacing = {word1:spaces,word2:spaces}
    spaces = [space,space,space]
    
    Based on the repetitions of each word, calculates
    the factors (in range) of the repetitions in order
    to detect possible sizes of keys.
    
    result = {factor:amount}
    amount = number of repetitions of the factor
    '''
    #rang: range of words size -> tuple = (from, to) -> it defines the size of the key
    possibleFactors = {}
    for i in range(rang[0],rang[1]):
        for key in dictSpacing.keys():
            spaces = dictSpacing[key]
            for space in spaces:
                if space % i == 0:
                    if i in possibleFactors.keys():
                        possibleFactors[i] += 1
                    else:
                        possibleFactors[i] = 1
    return possibleFactors

def summarizeFactors(listPossibleFactors):
    '''
    Given a list of possible factors, summarize all of them in one dictionary
    
    result = {factor:amount}
    amount = number of repetitions of the factor
    '''
    res = {}
    for possibleFactors in listPossibleFactors:
        for key in possibleFactors.keys():
            if key in res.keys():
                res[key] += possibleFactors[key]
            else:
                res[key] = possibleFactors[key]
    return res

def getHigher(factors):
    '''
    Based on the list of factors, gets the more frequent one
    '''
    higher = 0
    factor = None
    for key in factors.keys():
        if factors[key] > higher:
            higher = factors[key] 
            factor = key
    return factor

def calculateSizeKeyStatistics(factors):
    '''
    Calculates statistics for the possible sizes of keys
    
    result={factor:probability}
    '''
    total = 0
    stats = {}
    for key in factors.keys():
        total += factors[key]
    for key in factors.keys():
        stats[key] = 100*factors[key]/total
    return stats


def removeDuplicates(alph):
    '''
    Remove duplicates from an alphabet
    '''
    newAlph = []
    for c in alph:
        if c not in newAlph:
            newAlph.append(c)
    return "".join(newAlph)
        
def alphaToDict(alph, reverse=None):
    '''
    Based on an alphabet, returns a dictionary with
    the position of each letter in the alphabet
    '''
    if reverse:
        #pos as key, letter as value
        return dict([[i,x] for i, x in enumerate(alph)])
    else:
        #letter as key, pos as value
        return dict([[x,i] for i, x in enumerate(alph)])