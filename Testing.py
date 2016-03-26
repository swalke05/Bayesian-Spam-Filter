import sys
from decimal import *

numHam = 1721 #Total number of ham emails from learning phase
numSpam = 779 #Total number of spam emails from learning phase

#P(word|ham)
def getChanceHamContains(word, hamDictionary):
    estimate = -1

    
    for entry in hamDictionary:
        if (entry[0] == word):
            getcontext().prec = 3
            estimate = Decimal(entry[1])/Decimal(numHam)
            break
            
    return estimate

#P(word|spam)
def getChanceSpamContains(word, spamDictionary):
    pass


